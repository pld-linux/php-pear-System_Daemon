<?php
/* vim: set noai expandtab tabstop=4 softtabstop=4 shiftwidth=4: */
/**
 * System_Daemon turns PHP-CLI scripts into daemons.
 *
 * PHP version 5
 *
 * @category  System
 * @package   System_Daemon
 * @author    Elan Ruusamäe <glen@pld-linux.org>
 * @license   http://www.opensource.org/licenses/bsd-license.php New BSD Licence
 * @version   SVN: Release: $Id$
 * @link      http://trac.plutonia.nl/projects/system_daemon
 */

/**
 * A System_Daemon_OS driver for PLD Linux Operating Systems
 *
 * @category  System
 * @package   System_Daemon
 * @author    Elan Ruusamäe <glen@pld-linux.org>
 * @license   http://www.opensource.org/licenses/bsd-license.php New BSD Licence
 * @version   SVN: Release: $Id$
 * @link      http://trac.plutonia.nl/projects/system_daemon
 * *
 */
class System_Daemon_OS_PLD extends System_Daemon_OS_Linux
{
    /**
     * On Linux, a distro-specific version file is often telling us enough
     *
     * @var string
     */
    protected $_osVersionFile = "/etc/pld-release";

    /**
     * Path of init.d scripts
     *
     * @var string
     */
    protected $_autoRunDir = '/etc/rc.d/init.d';

    /**
     * Template path
     *
     * @var string
     */
    protected $_autoRunTemplatePath = '#datadir#/template_PLD';

    /**
     * Replace the following keys with values to convert a template into
     * a read autorun script
     *
     * @var array
     */
    protected $_autoRunTemplateReplace = array(
        "@author_name@"  => "{PROPERTIES.authorName}",
        "@author_email@" => "{PROPERTIES.authorEmail}",
        '@name@'         => '{PROPERTIES.appName}',
        '@desc@'         => '{PROPERTIES.appDescription}',
        '@bin_file@'     => '{PROPERTIES.appDir}/{PROPERTIES.appExecutable}',
        '@bin_name@'     => '{PROPERTIES.appExecutable}',
        '@pid_file@'     => '{PROPERTIES.appPidLocation}',
        '@chkconfig@'    => '{PROPERTIES.appChkConfig}',
    );

}
