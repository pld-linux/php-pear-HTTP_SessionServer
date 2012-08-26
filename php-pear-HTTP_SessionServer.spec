%define		_class		HTTP
%define		_subclass	SessionServer
%define		_status		alpha
%define		_pearname	HTTP_SessionServer
%include	/usr/lib/rpm/macros.php
Summary:	%{_pearname} - daemon to store session data
Summary(pl.UTF-8):	%{_pearname} - demon do przechowywania danych sesji
Name:		php-pear-%{_pearname}
Version:	0.5.0
Release:	6
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	52ec43a814aea36fa16f94a122e3fbc3
URL:		http://pear.php.net/package/HTTP_SessionServer/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.300
Requires:	php(core) >= 4.3.0
Requires:	php(pcntl)
Requires:	php-pear
Requires:	php-pear-Net_Server >= 0.12.0
Requires:	php-pear-Net_Socket
Requires:	php-pear-PEAR-core
Suggests:	php-pear-DB
Suggests:	php-pear-MDB2 >= 1:2.0.0-0.RC1
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# exclude optional dependencies
%define		_noautoreq	'pear(DB.*)' 'pear(MDB2.*)'

%description
HTTP_SessionServer is a simple PHP based daemon that helps you
maintaining state between physically different hosts.

HTTP_SessionServer implements a very simple protocol to store and
retrieve data on the server. The storage backend is driver based,
currently only a storage for the filesystem has been implemented, but
you may easily change this.

HTTP_SessionServer comes with a matching client implementation using
Net_Socket as well as a session save handler.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
HTTP_SeesionServer jest prostym, opartym na PHP daemonem wspomagającym
przetwarzanie stanu sesji pomiędzy dwoma serwerami.

HTTP_SessionServer zawiera zaimplementowany prosty protokół do zapisu
i odczytu danych na serwerze. Backend do zapisu jest oparty na
sterownikach, obecnie możliwy jest zapis tylko do pliku.

HTTP_SessionServer jest dostarczany z klientem zaimplementowanym przy
użyciu Net_Socket jak również z obsługą zapisu sesji.

Ta klasa ma w PEAR status: %{_status}.

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
%doc install.log optional-packages.txt
%doc docs/%{_pearname}/{docs,examples}
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/HTTP/*.php
%{php_pear_dir}/HTTP/SessionServer
