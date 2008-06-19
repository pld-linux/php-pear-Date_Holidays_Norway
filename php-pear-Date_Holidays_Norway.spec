%include	/usr/lib/rpm/macros.php
%define		_class		Date
%define		_subclass	Holidays_Norway
%define		_status		alpha
%define		_pearname	Date_Holidays_Norway
Summary:	%{_pearname} - Driver based class to calculate holidays in Norway
Summary(pl.UTF-8):	%{_pearname} - klasa do obliczania świąt norweskich
Name:		php-pear-%{_pearname}
Version:	0.1.0
Release:	1
License:	PHP License
Group:		Development/Languages/PHP
Source0:	http://pear.php.net/get/%{_pearname}-%{version}.tgz
# Source0-md5:	f0193c61b94b7f70b6e751b5ef5d85f6
Patch0:		%{name}-paths.patch
URL:		http://pear.php.net/package/Date_Holidays_Norway/
BuildRequires:	php-pear-PEAR
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
Requires:	php-pear
Requires:	php-pear-Date_Holidays >= 0.18.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Date_Holidays helps you calculate the dates and titles of holidays and
other special celebrations. This is the driver for calculating
holidays in Norway.

In PEAR status of this package is: %{_status}.

%description -l pl.UTF-8
Date_Holidays pozwala na obliczenie dat oraz tytułów świąt oraz
specjalnych okazji. Klasa ta pozwala na wyliczenie świąt norweskich.

Ta klasa ma w PEAR status: %{_status}.

%prep
%pear_package_setup
%patch0 -p1

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{php_pear_dir}
%pear_package_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc install.log
%{php_pear_dir}/.registry/*.reg
%{php_pear_dir}/Date/Holidays/Driver/Norway.php
