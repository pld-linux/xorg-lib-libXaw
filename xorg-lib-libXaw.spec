#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	X Athena Widgets library
Summary(pl.UTF-8):	Biblioteka X Athena Widgets
Name:		xorg-lib-libXaw
Version:	1.0.5
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
# Source0-md5:	64e7782db4653cb57c7f7e660b2431c3
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

%description -l pl.UTF-8
Biblioteka X Athena Widgets.

%package devel
Summary:	Header files for libXaw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXaw
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

%description devel -l pl.UTF-8
Biblioteka X Athena Widgets.

Pakiet zawiera pliki nagłówkowe niezbędne do kompilowania programów
używających biblioteki libXaw.

%package static
Summary:	Static libXaw library
Summary(pl.UTF-8):	Biblioteka statyczna libXaw
Group:		X11/Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}
Obsoletes:	libXaw-static

%description static
X Athena Widgets library.

This package contains the static libXaw library.

%description static -l pl.UTF-8
Biblioteka X Athena Widgets.

Pakiet zawiera statyczną bibliotekę libXaw.

%prep
%setup -q -n libXaw-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}

%configure \
	%{!?with_static_libs:--disable-static}
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
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXaw6.so.6.*.*
%attr(755,root,root) %{_libdir}/libXaw7.so.7.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXaw6.so
%attr(755,root,root) %{_libdir}/libXaw7.so
%attr(755,root,root) %{_libdir}/libXaw.so
%{_libdir}/libXaw6.la
%{_libdir}/libXaw7.la
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*.h
%{_includedir}/X11/Xaw/Template.c
%{_pkgconfigdir}/xaw6.pc
%{_pkgconfigdir}/xaw7.pc
%{_mandir}/man3/*.3x*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw6.a
%{_libdir}/libXaw7.a
%endif
