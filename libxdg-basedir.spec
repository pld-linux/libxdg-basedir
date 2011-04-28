Summary:	An implementation of the XDG Base Directory specification
Summary(pl.UTF-8):	Implementacja specyfikacji XDG Base Directory
Name:		libxdg-basedir
Version:	1.1.1
Release:	2
License:	MIT
Group:		Libraries
Source0:	http://n.ethz.ch/~nevillm/download/libxdg-basedir/%{name}-%{version}.tar.gz
# Source0-md5:	7c64a28b08c8fdf6c8a95b0d5f1497b0
URL:		http://n.ethz.ch/~nevillm/download/libxdg-basedir/
BuildRequires:	autoconf
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
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for libxdg-basedir library.

%description devel -l pl.UTF-8
Pliki nagłówkowe biblioteki libxdg-basedir.

%package static
Summary:	Static libxdg-basedir library
Summary(pl.UTF-8):	Statyczna biblioteka libxdg-basedir.
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libxdg-basedir library.

%description static -l pl.UTF-8
Statyczna biblioteka libxdg-basedir.

%prep
%setup -q

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
%attr(755,root,root) %{_libdir}/%{name}.so.*.*
%attr(755,root,root) %ghost %{_libdir}/%{name}.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/%{name}.so
%{_includedir}/basedir.h
%{_includedir}/basedir_fs.h
%{_pkgconfigdir}/%{name}.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/%{name}.a
