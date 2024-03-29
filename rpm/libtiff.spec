Name:       libtiff
Summary:    Library of functions for manipulating TIFF format image files
Version:    4.6.0
Release:    1
License:    libtiff
URL:        https://github.com/sailfishos/libtiff
Source0:    %{name}-%{version}.tar.gz
Patch0:     0001-Prevent-some-out-of-memory-attacks.patch
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libjpeg-devel
BuildRequires:  automake autoconf libtool

%description
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package devel
Summary:    Development tools for programs which will use the libtiff library
Requires:   %{name} = %{version}-%{release}

%description devel
This package contains the header files and documentation necessary for
developing programs which will manipulate TIFF format image files
using the libtiff library.

If you need to develop programs which will manipulate TIFF format
image files, you should install this package.  You'll also need to
install the libtiff package.

%package tools
Summary:    Command-line utility programs for manipulating TIFF files
Requires:   %{name} = %{version}-%{release}

%description tools
This package contains command-line programs for manipulating TIFF format
image files using the libtiff library.

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man and info pages for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/upstream

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
sed -i "s/for file.*/for false/g" autogen.sh
./autogen.sh
%configure --disable-static
%make_build

%install
%make_install

# no libGL dependency, please
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffgt

# no sgi2tiff or tiffsv, either
rm -f $RPM_BUILD_ROOT%{_bindir}/sgi2tiff
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffsv

mv $RPM_BUILD_ROOT%{_docdir}/tiff-* \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
rm $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/LICENSE.md
ln -s ../../licenses/%{name}-%{version}/LICENSE.md \
   $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/LICENSE.md


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license LICENSE.md
%{_libdir}/%{name}.so.*
%{_libdir}/%{name}xx.so.*

%files devel
%defattr(-,root,root,-)
%{_includedir}/*
%{_libdir}/%{name}.so
%{_libdir}/%{name}xx.so
%{_libdir}/pkgconfig/%{name}-4.pc

%files tools
%defattr(-,root,root,-)
%{_bindir}/*

%files doc
%defattr(-,root,root,-)
%{_docdir}/%{name}-%{version}
