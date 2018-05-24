Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.8
Release: 1
License: MIT
Group: System/Libraries
Source0: ftp://xmlsoft.org/libxml2/%{name}-%{version}.tar.gz
Patch1: 0001-Suppress-documentation-installation-as-it-causes-pro.patch

BuildRequires: zlib-devel
URL: http://xmlsoft.org/

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

%package python-build
Summary: Package for building python extensions
Group: Development/Libraries
Requires: libxml2-devel = %{version}-%{release}

%description python-build
%{summary}

%package devel
Summary: Libraries, includes, etc. to develop XML and HTML applications
Group: Development/Libraries
Requires: libxml2 = %{version}-%{release}
Requires: zlib-devel
Requires: pkgconfig

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
%setup -q -n %{name}-%{version}/libxml2
# 0001-Suppress-documentation-installation-as-it-causes-pro.patch
%patch1 -p1

%build
%autogen --with-python=no
make %{_smp_mflags}
gzip -9 ChangeLog

%install
rm -fr %{buildroot}

%makeinstall
gzip -9 doc/libxml2-api.xml
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
touch -m --reference=$RPM_BUILD_ROOT/%{_includedir}/libxml2/libxml/parser.h $RPM_BUILD_ROOT/%{_bindir}/xml2-config
(cd doc/examples ; make clean ; rm -rf .deps Makefile)

%clean
rm -fr %{buildroot}

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)

%doc AUTHORS Copyright
%doc %{_mandir}/man1/xml2-config.1*
%doc %{_mandir}/man3/libxml.3*

%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%defattr(-, root, root)
%doc ChangeLog.gz NEWS README TODO

%{_libdir}/lib*.so
#needed to build python
%{_libdir}/*.sh
%{_includedir}/*
%{_bindir}/xml2-config
%{_datadir}/aclocal/libxml.m4
%{_libdir}/pkgconfig/libxml-2.0.pc
%{_libdir}/cmake/%{name}/%{name}-config.cmake

%files python-build
%defattr(-, root, root,-)
%{_libdir}/libxml2.la
