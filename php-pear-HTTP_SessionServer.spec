%include	/usr/lib/rpm/macros.php
%define		_class		HTTP
%define		_subclass	SessionServer
%define		_status		alpha
%define		_pearname	%{_class}_%{_subclass}

Summary:	%{_pearname} - daemon to store session data
Summary(pl):	%{_pearname} - demon do przechowywania danych sesji
Name:		php-pear-%{_pearname}
Version:	0.4.0
Release:	1
License:	PHP 2.02
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	71ff19663cee9e427e0d6db1c83a1d35
URL:		http://pear.php.net/package/HTTP_SessionServer/
BuildRequires:	rpm-php-pearprov >= 4.0.2-98
Requires:	php-pear
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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

%description -l pl
HTTP_SeesionServer jest prostym, opartym na PHP daemonem wspomagaj±cym
przetwarzanie stanu sesji pomiêdzy dwoma serwerami.

HTTP_SessionServer zawiera zaimplementowany prosty protokó³ do zapisu
i odczytu danych na serwerze. Backend do zapisu jest oparty na
sterownikach, obecnie mo¿liwy jest zapis tylko do pliku.

HTTP_SessionServer jest dostarczany z klientem zaimplementowanym przy
u¿yciu Net_Socket jak równie¿ z obs³ug± zapisu sesji.

Ta klasa ma w PEAR status: %{_status}.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

install %{_pearname}-%{version}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}
install %{_pearname}-%{version}/%{_subclass}/*.php $RPM_BUILD_ROOT%{php_pear_dir}/%{_class}/%{_subclass}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc %{_pearname}-%{version}/{docs,examples}
%{php_pear_dir}/%{_class}/*.php
%{php_pear_dir}/%{_class}/%{_subclass}
