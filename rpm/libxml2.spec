Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.13.4
Release: 1
License: MIT
Source0: %{name}-%{version}.tar.gz
Patch1: 0001-Disable-documentation-further.patch
Patch2: 0002-dict-Add-fallback-if-getentropy-is-not-supported.patch

BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: pkgconfig(zlib)
URL: https://github.com/sailfishos/libxml2
Obsoletes: libxml2-python-build
Conflicts: libxml2-python-build
Obsoletes: libxml2-doc
Conflicts: libxml2-doc

%description 
This library allows to manipulate XML files. It includes support 
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%package devel
Summary: Libraries, includes, etc. to develop XML and HTML applications
Requires: libxml2 = %{version}-%{release}
Requires: pkgconfig(zlib)

%description devel
Libraries, include files, etc you can use to develop XML applications.
This library allows to manipulate XML files. It includes support 
to read, modify and write XML and HTML files. There is DTDs support
this includes parsing and validation even with complex DtDs, either
at parse time or later once the document has been modified. The output
can be a simple SAX stream or and in-memory DOM like representations.
In this case one can use the built-in XPath and XPointer implementation
to select subnodes or ranges. A flexible Input/Output mechanism is
available, with existing HTTP and FTP modules and combined to an
URI library.

%prep
%autosetup -p1 -n %{name}-%{version}/libxml2

%build
%autogen --with-python=no --with-zlib --with-icu=no --with-http
%make_build

%install

%makeinstall
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
touch -m --reference=$RPM_BUILD_ROOT/%{_includedir}/libxml2/libxml/parser.h $RPM_BUILD_ROOT/%{_bindir}/xml2-config

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license Copyright
%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%{_libdir}/lib*.so
%{_includedir}/*
%{_bindir}/xml2-config
%{_datadir}/aclocal/libxml.m4
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/%{name}/%{name}-config.cmake
%exclude %{_libdir}/*.la
