# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.24
# 

Name:       libtiff

# >> macros
# << macros

Summary:    Library of functions for manipulating TIFF format image files
Version:    4.0.2
Release:    1
Group:      System/Libraries
License:    libtiff
URL:        http://www.libtiff.org/
Source0:    http://download.osgeo.org/libtiff/tiff-%{version}.tar.gz
Source100:  libtiff.yaml
Patch0:     libtiff-4.0.2-tiff2pdf.patch
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



%prep
%setup -q -n tiff-%{version}

# libtiff-4.0.2-tiff2pdf.patch
%patch0 -p1
# >> setup
# << setup

%build
# >> build pre
export CFLAGS="%{optflags} -fno-strict-aliasing"
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre

# << install pre
%make_install

# >> install post

# remove what we didn't want installed
rm -rf $RPM_BUILD_ROOT%{_datadir}/doc/

# no libGL dependency, please
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffgt
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffgt.1
rm -f html/man/tiffgt.1.html

# no sgi2tiff or tiffsv, either
rm -f $RPM_BUILD_ROOT%{_bindir}/sgi2tiff
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/sgi2tiff.1
rm -f html/man/sgi2tiff.1.html
rm -f $RPM_BUILD_ROOT%{_bindir}/tiffsv
rm -f $RPM_BUILD_ROOT%{_mandir}/man1/tiffsv.1
rm -f html/man/tiffsv.1.html

# don't include documentation Makefiles, they are a multilib hazard
find html -name 'Makefile*' | xargs rm

# << install post


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%defattr(-,root,root,0755)
%doc COPYRIGHT README RELEASE-DATE VERSION
%{_bindir}/*
%{_libdir}/libtiff.so.*
%{_libdir}/libtiffxx.so.*
%doc %{_mandir}/man1/*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%defattr(-,root,root,0755)
%doc TODO ChangeLog html
%{_includedir}/*
%{_libdir}/libtiff.so
%{_libdir}/libtiffxx.so
%doc %{_mandir}/man3/*
%{_libdir}/pkgconfig/libtiff-4.pc
# << files devel
