Summary: Library providing XML and HTML support
Name: libxml2
Version: 2.9.12
Release: 1
License: MIT
Source0: %{name}-%{version}.tar.gz
Patch1: 0001-Suppress-documentation-installation-as-it-causes-pro.patch

BuildRequires: autoconf
BuildRequires: libtool
BuildRequires: pkgconfig(zlib)
URL: https://github.com/sailfishos/libxml2

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
Requires: libxml2-devel = %{version}-%{release}

%description python-build
%{summary}

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

%package doc
Summary:   Documentation for %{name}
Requires:  %{name} = %{version}-%{release}

%description doc
Man pages for %{name}.

%prep
%autosetup -p1 -n %{name}-%{version}/libxml2

%build
%autogen --with-python=no --with-zlib --with-icu=no
%make_build
gzip -9 ChangeLog

%install
rm -fr %{buildroot}

%makeinstall
gzip -9 doc/libxml2-api.xml
rm -f $RPM_BUILD_ROOT%{_libdir}/*.a

# multiarch crazyness on timestamp differences or Makefile/binaries for examples
touch -m --reference=$RPM_BUILD_ROOT/%{_includedir}/libxml2/libxml/parser.h $RPM_BUILD_ROOT/%{_bindir}/xml2-config

mkdir -p $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}
install -m0644 -t $RPM_BUILD_ROOT%{_docdir}/%{name}-%{version}/ \
    AUTHORS ChangeLog.gz CONTRIBUTING MAINTAINERS NEWS README TODO

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%license Copyright
%{_libdir}/lib*.so.*
%{_bindir}/xmllint
%{_bindir}/xmlcatalog

%files devel
%defattr(-, root, root)

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

%files doc
%defattr(-, root, root)
%doc %{_docdir}/%{name}-%{version}/*
%doc %{_mandir}/man1/xml2-config.1*
%doc %{_mandir}/man3/libxml.3*
