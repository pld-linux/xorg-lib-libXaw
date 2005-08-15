
#
Summary:	X Athena Widgets library
Summary(pl):	Biblioteka X Athena Widgets
Name:		xorg-lib-libXaw
Version:	0.99.0
Release:	0.03
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/X11R7.0-RC0/lib/libXaw-%{version}.tar.bz2
# Source0-md5:	84b2766703f7b1d150edc21b338856de
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	libtool
BuildRequires:	pkg-config
BuildRequires:	xorg-util-util-macros
BuildRoot:	%{tmpdir}/libXaw-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
X Athena Widgets library.

%description -l pl
Biblioteka X Athena Widgets.


%package devel
Summary:	Header files libXaw development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXaw
Group:		X11/Development/Libraries
Requires:	xorg-lib-libXaw = %{version}-%{release}
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXpm-devel

%description devel
X Athena Widgets library.

This package contains the header files needed to develop programs that
use these libXaw.

%description devel -l pl
Biblioteka X Athena Widgets.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXaw.


%package static
Summary:	Static libXaw libraries
Summary(pl):	Biblioteki statyczne libXaw
Group:		Development/Libraries
Requires:	xorg-lib-libXaw-devel = %{version}-%{release}

%description static
X Athena Widgets library.

This package contains the static libXaw library.

%description static -l pl
Biblioteka X Athena Widgets.

Pakiet zawiera statyczn± bibliotekê libXaw.


%prep
%setup -q -n libXaw-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	pkgconfigdir=%{_pkgconfigdir} \
	aclocaldir=%{_aclocaldir}


%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc ChangeLog README
%attr(755,root,wheel) %{_libdir}/libXaw*.so.*


%files devel
%defattr(644,root,root,755)
%{_includedir}/X11/Xaw/*.h
%{_libdir}/libXaw*.la
%attr(755,root,wheel) %{_libdir}/libXaw*.so
%{_aclocaldir}/xaw.m4
%{_pkgconfigdir}/xaw*.pc
%{_mandir}/man3/*.3*


%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw*.a
