%include	/usr/lib/rpm/macros.php
%define		_class		System
%define		_subclass	Daemon
%define		_status		alpha
%define		_pearname	System_Daemon
Summary:	%{_pearname} - Turn PHP scripts into Linux daemons
Summary(pl.UTF-8):	%{_pearname} - zamiana skryptów PHP w demony
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	1
License:	New BSD License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	d136658fb1a260b11111940c28c29d16
URL:		http://pear.php.net/package/System_Daemon/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(Log.*)'

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

In PEAR status of this package is: %{_status}.

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

Ta klasa ma w PEAR status: %{_status}.

%package tests
Summary:	Tests for PEAR::%{_pearname}
Summary(pl.UTF-8):	Testy dla PEAR::%{_pearname}
Group:		Development/Languages/PHP
AutoReq:	no
Requires:	%{name} = %{version}-%{release}
AutoProv:	no

%description tests
Tests for PEAR::%{_pearname}.

%description tests -l pl.UTF-8
Testy dla PEAR::%{_pearname}.

%prep
%pear_package_setup

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%post
if [ -f %{_docdir}/%{name}-%{version}/optional-packages.txt ]; then
	cat %{_docdir}/%{name}-%{version}/optional-packages.txt
fi

%files
%defattr(644,root,root,755)
%doc install.log
%doc docs/System_Daemon/{docs,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/System/Daemon
%{php_pear_dir}/System/Daemon.php
%{php_pear_dir}/tools/changelog_gen.php
%{php_pear_dir}/tools/package_gen.php
%{php_pear_dir}/package.php
%{php_pear_dir}/test.php
%{php_pear_dir}/data/System_Daemon

%files tests
%defattr(644,root,root,755)
%{php_pear_dir}/tests/System_Daemon
