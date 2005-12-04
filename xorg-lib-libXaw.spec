Summary:	X Athena Widgets library
Summary(pl):	Biblioteka X Athena Widgets
Name:		xorg-lib-libXaw
Version:	0.99.3
Release:	0.1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/X11R7.0-RC3/lib/libXaw-%{version}.tar.bz2
# Source0-md5:	250612be2f9a83739a465407e21fc21d
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	ed
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
Obsoletes:	libXaw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Athena Widgets library.

%description -l pl
Biblioteka X Athena Widgets.

%package devel
Summary:	Header files for libXaw library
Summary(pl):	Pliki nag³ówkowe biblioteki libXaw
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXpm-devel
Obsoletes:	libXaw-devel

%description devel
X Athena Widgets library.

This package contains the header files needed to develop programs that
use libXaw.

%description devel -l pl
Biblioteka X Athena Widgets.

Pakiet zawiera pliki nag³ówkowe niezbêdne do kompilowania programów
u¿ywaj±cych biblioteki libXaw.

%package static
Summary:	Static libXaw library
Summary(pl):	Biblioteka statyczna libXaw
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXaw-static

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
%attr(755,root,root) %{_libdir}/libXaw6.so.6.*.*
%attr(755,root,root) %{_libdir}/libXaw7.so.7.*.*
%attr(755,root,root) %{_libdir}/libXaw8.so.8.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXaw6.so
%attr(755,root,root) %{_libdir}/libXaw7.so
%attr(755,root,root) %{_libdir}/libXaw8.so
%attr(755,root,root) %{_libdir}/libXaw.so
%{_libdir}/libXaw6.la
%{_libdir}/libXaw7.la
%{_libdir}/libXaw8.la
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*.h
%{_includedir}/X11/Xaw/Template.c
%{_aclocaldir}/xaw.m4
%{_pkgconfigdir}/xaw6.pc
%{_pkgconfigdir}/xaw7.pc
%{_pkgconfigdir}/xaw8.pc
%{_mandir}/man3/*.3x*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw6.a
%{_libdir}/libXaw7.a
%{_libdir}/libXaw8.a
