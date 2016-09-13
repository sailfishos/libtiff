Name:       libtiff
Summary:    Library of functions for manipulating TIFF format image files
Version:    4.0.6
Release:    1
Group:      System/Libraries
License:    libtiff
URL:        http://www.remotesensing.org/libtiff/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig
BuildRequires:  pkgconfig(zlib)
BuildRequires:  libjpeg-devel

%description
The libtiff package contains a library of functions for manipulating
TIFF (Tagged Image File Format) image format files.  TIFF is a widely
used file format for bitmapped images.  TIFF files usually end in the
.tif extension and they are often quite large.

The libtiff package should be installed if you need to manipulate TIFF
format image files.

%package devel
Summary:    Development tools for programs which will use the libtiff library
Group:      Development/Libraries
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
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description tools
This package contains command-line programs for manipulating TIFF format
image files using the libtiff library.

%prep
%setup -q -n %{name}-%{version}/%{name}

%build
export CFLAGS="%{optflags} -fno-strict-aliasing"
%configure --disable-static
make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install

# remove what we didn't want installed
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/

# no libGL dependency, please
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffgt

# no sgi2tiff or tiffsv, either
rm -f $RPM_BUILD_ROOT%{_bindir}/sgi2tiff
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffsv

rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffgt.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/sgi2tiff.1
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffsv.1

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc COPYRIGHT
%{_libdir}/libtiff.so.*
%{_libdir}/libtiffxx.so.*

%files devel
%defattr(-,root,root,-)
%doc TODO ChangeLog README RELEASE-DATE VERSION
%{_includedir}/*
%{_libdir}/libtiff.so
%{_libdir}/libtiffxx.so
%doc %{_mandir}/man3/*
%doc %{_mandir}/man1/*
%{_libdir}/pkgconfig/libtiff-4.pc

%files tools
%defattr(-,root,root,-)
%{_bindir}/*
%{_mandir}/man1/*
