%define		status		stable
%define		pearname	System_Daemon
Summary:	%{pearname} - Turn PHP scripts into Linux daemons
Summary(pl.UTF-8):	%{pearname} - zamiana skryptów PHP w demony
Name:		php-pear-%{pearname}
Version:	1.0.0
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{pearname}-%{version}.tgz
# Source0-md5:	95b8a56bf6e92ad9daa2d3703bd2ba67
Source1:	PLD.php
Source2:	template_PLD.sh
URL:		http://pear.php.net/package/System_Daemon/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.580
Requires:	php-pear
Suggests:	php-pear-Log
Obsoletes:	php-pear-System_Daemon-tests
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	pear(Log.*)

%description
System_Daemon is a PHP class that allows developers to create their
own daemon applications on Linux systems.

The class is focussed entirely on creating and spawning standalone
daemons, and for example includes:
 - Methods to generate OS-specific startup-files (init.d) (currently
   only Debian/Ubuntu are supported), so that your application gets
   started on reboot as well,
 - Methods for logging purposes,
 - Simple syntax,
 - Support for PEAR's Log package,
 - Can run with or without PEAR (PEAR adds more elegance and
   functionality),
 - Default signal handlers, but optionally reroute signals to your own
   handlers,
 - Log levels comply with PEAR_LOG_ levels but are called
   SYSTEM_DAEMON_LOG_ for (in)dependency reasons,
 - Set options like max RAM usage

In PEAR status of this package is: %{status}.

%description -l pl.UTF-8
System_Daemon to klasa PHP pozwalająca programiście na tworzenie w
systemach unixowych aplikacji działających jako demony.

Klasa ta zajmuje się wyłącznie tworzeniem i uruchamianiem
samodzielnych demonów. Inna funkcjonalność to między innymi:
 - metody do generowania plików startowych (init.d), tak aby aplikacja
   uruchamiana była także przy restarcie systemu,
 - metody do obsługi logowania komunikatów,
 - prosta składnia,
 - może działać bez PEAR (wraz z PEAR dostępna dodatkowa
   funkcjonalność),
 - domyślna obsługa sygnałów, opcjonalnie przekazanie sygnałów to
   własnych funkcji,
 - poziomy komunikatów kompatybilne z PEAR_LOG_ ale nazwane
   SYSTME_DAEMON_LOG_ dla zachowania niezależności od PEAR,
 - ustawianie opcji takich jak maksymalne wykorzystanie pamięci RAM.

Ta klasa ma w PEAR status: %{status}.

%prep
%pear_package_setup

# examples fixups
mv docs/%{pearname}/examples .

# pear/docs -> docs
mv docs/%{pearname}/docs/* docs
rmdir docs/System_Daemon/docs docs/System_Daemon

# not part of the package, some tools to make _this_ pear package.
rm -rf ./%{php_pear_dir}/tools
rm -f ./%{php_pear_dir}/{package,test}.php

mv .%{php_pear_dir}/README.md .

# duplicate: we also package these
rm -rf examples/System

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir}}
%pear_package_install

# Add PLD Linux OS system
cp -a %{SOURCE1} $RPM_BUILD_ROOT%{php_pear_dir}/System/Daemon/OS
cp -a %{SOURCE2} $RPM_BUILD_ROOT%{php_pear_dir}/data/System_Daemon/data/template_PLD

install -d $RPM_BUILD_ROOT{%{php_pear_dir},%{_bindir},%{_examplesdir}/%{name}-%{version}}
cp -a examples/*  $RPM_BUILD_ROOT%{_examplesdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%post -p <lua>
%pear_package_print_optionalpackages

%files
%defattr(644,root,root,755)
%doc install.log optional-packages.txt
%doc README.md
%doc docs/*
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/System/Daemon
%{php_pear_dir}/System/Daemon.php
%{php_pear_dir}/data/System_Daemon

%{_examplesdir}/%{name}-%{version}
