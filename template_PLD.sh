#!/bin/sh
#
# chkconfig:	@chkconfig@
#
# description:	@desc@
#
# processname:	@name@
# config:
# pidfile: @pid_file@
#
# $Id$

# Source function library
. /etc/rc.d/init.d/functions

# Get network config
. /etc/sysconfig/network

# Check that networking is up.
if is_yes "${NETWORKING}"; then
	if [ ! -f /var/lock/subsys/network -a "$1" != stop -a "$1" != status ]; then
		msg_network_down "@name@"
		exit 1
	fi
else
	exit 0
fi

# Get service config - may override defaults
[ -f /etc/sysconfig/@name@ ] && . /etc/sysconfig/@name@

start() {
	# Check if the service is already running?
	if [ -f /var/lock/subsys/@name@ ]; then
		msg_already_running "@name@"
		return
	fi

	msg_starting "@name@"
	daemon @bin_file@
	RETVAL=$?
	[ $RETVAL -eq 0 ] && touch /var/lock/subsys/@name@
}

stop() {
	if [ ! -f /var/lock/subsys/@name@ ]; then
		msg_not_running "@name@"
		return
	fi

	# Stop daemons.
	msg_stopping "@name@"
	killproc --pidfile @pid_file@ @bin_name@ -TERM
	rm -f /var/lock/subsys/@name@
}

condrestart() {
	if [ ! -f /var/lock/subsys/@name@ ]; then
		msg_not_running "@name@"
		RETVAL=$1
		return
	fi

	stop
	start
}

RETVAL=0
# See how we were called.
case "$1" in
  start)
	start
	;;
  stop)
	stop
	;;
  restart)
	stop
	start
	;;
  try-restart)
	condrestart 0
	;;
  force-reload)
	condrestart 7
	;;
  status)
	status --pidfile @pid_file@ @name@ @bin_name@
	RETVAL=$?
	;;
  *)
	msg_usage "$0 {start|stop|restart|try-restart|reload|force-reload|status}"
	exit 3
esac

exit $RETVAL
