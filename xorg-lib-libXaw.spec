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
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 0.19
BuildRequires:	xorg-lib-libXmu-devel
BuildRequires:	xorg-lib-libXp-devel
BuildRequires:	xorg-lib-libXpm-devel
BuildRequires:	xorg-util-util-macros
Obsoletes:	libXaw
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X Athena Widgets library.

%description -l pl
Biblioteka X Athena Widgets.

%package devel
Summary:	Header files libXaw development
Summary(pl):	Pliki nag³ówkowe do biblioteki libXaw
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	xorg-lib-libXmu-devel
Requires:	xorg-lib-libXp-devel
Requires:	xorg-lib-libXpm-devel
Obsoletes:	libXaw-devel

%description devel
X Athena Widgets library.

This package contains the header files needed to develop programs that
use these libXaw.

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
%attr(755,root,root) %{_libdir}/libXaw*.so.*.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libXaw*.so
%{_libdir}/libXaw*.la
%{_includedir}/X11/Xaw/*.h
%{_aclocaldir}/xaw.m4
%{_pkgconfigdir}/xaw*.pc
%{_mandir}/man3/*.3*

%files static
%defattr(644,root,root,755)
%{_libdir}/libXaw*.a
