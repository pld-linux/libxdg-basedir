Summary:	An implementation of the XDG Base Directory specification
Summary(pl.UTF-8):	Implementacja specyfikacji XDG Base Directory
Name:		libxdg-basedir
Version:	1.2.3
Release:	1
License:	MIT
Group:		Libraries
#Source0Download: https://github.com/devnev/libxdg-basedir/tags
Source0:	https://github.com/devnev/libxdg-basedir/archive/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	6fee7e4ce612f79dacfc8867687737ac
URL:		https://github.com/devnev/libxdg-basedir
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
An implementation of the XDG Base Directory specification.

%description -l pl.UTF-8
Implementacja specyfikacji XDG Base Directory.

%package devel
Summary:	Header files for libxdg-basedir library
Summary(pl.UTF-8):	Pliki nagłówkowe biblioteki libxdg-basedir
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}

%description devel
Header files for libxdg-basedir library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxdg-basedir.

%package static
Summary:	Static libxdg-basedir library
Summary(pl.UTF-8):	Statyczna biblioteka libxdg-basedir.
Group:		Development/Libraries
Requires:	%{name}-devel%{?_isa} = %{version}-%{release}

%description static
Static libxdg-basedir library.

%description static -l pl.UTF-8
Statyczna biblioteka libxdg-basedir.

%prep
%setup -q -n %{name}-%{name}-%{version}

%build
%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__autoheader}
%{__automake}

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/libxdg-basedir.la

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc COPYING README.md
%{_libdir}/libxdg-basedir.so.*.*
%ghost %{_libdir}/libxdg-basedir.so.1

%files devel
%defattr(644,root,root,755)
%{_libdir}/libxdg-basedir.so
%{_includedir}/basedir.h
%{_includedir}/basedir_fs.h
%{_pkgconfigdir}/libxdg-basedir.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/libxdg-basedir.a
