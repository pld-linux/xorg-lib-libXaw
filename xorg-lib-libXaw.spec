#
# Conditional build:
%bcond_without	static_libs	# don't build static library
#
Summary:	X Athena Widgets library
Summary(pl.UTF-8):	Biblioteka X Athena Widgets
Name:		xorg-lib-libXaw
Version:	1.0.12
Release:	1
License:	MIT
Group:		X11/Libraries
Source0:	http://xorg.freedesktop.org/releases/individual/lib/libXaw-%{version}.tar.bz2
# Source0-md5:	7446f5fba888672aad068b29c0928ba3
Patch0:		format-security.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	docbook-dtd43-xml
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	xmlto >= 0.0.22
BuildRequires:	xorg-lib-libXext-devel
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-lib-libXt-devel
BuildRequires:	xorg-sgml-doctools >= 1.8
BuildRequires:	xorg-util-util-macros >= 1.12
Obsoletes:	libXaw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Athena Widgets library. Athena Widget Set is baced on the X Toolkit
Intrinsics (Xt) library.

%description -l pl.UTF-8
Biblioteka X Athena Widgets. Zestaw widgetów Athena jest oparty na
bibliotece X Toolkit Intrinsics (Xt).

%package devel
Summary:	Header files for libXaw library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libXaw
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXext-devel
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXpm-devel
Requires:	xorg-lib-libXt-devel
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
%patch0 -p1

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

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libXaw[67].so.[67]
/sbin/ldconfig -n $RPM_BUILD_ROOT%{_libdir}

%{__rm} -r $RPM_BUILD_ROOT{%{_docdir}/libXaw,%{_libdir}/libXaw[67].la}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/libXaw6.so.6.*.*
%attr(755,root,root) %ghost %{_libdir}/libXaw.so.6
%attr(755,root,root) %{_libdir}/libXaw7.so.7.*.*
%attr(755,root,root) %ghost %{_libdir}/libXaw.so.7

%files devel
%defattr(644,root,root,755)
%doc specs/libXaw.html
%attr(755,root,root) %{_libdir}/libXaw6.so
%attr(755,root,root) %{_libdir}/libXaw7.so
%attr(755,root,root) %{_libdir}/libXaw.so
%dir %{_includedir}/X11/Xaw
%{_includedir}/X11/Xaw/*.h
%{_includedir}/X11/Xaw/Template.c
%{_pkgconfigdir}/xaw6.pc
%{_pkgconfigdir}/xaw7.pc
%{_mandir}/man3/Xaw.3x*

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw6.a
%{_libdir}/libXaw7.a
%endif
