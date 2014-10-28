Summary: Python bindings for the libxml2 library
Name: libxml2-python
Version: 2.9.1
Release: 1
License: MIT
Group: System/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
# https://bugzilla.redhat.com/show_bug.cgi?id=877567
Patch1: libxml2-2.9.0-do-not-check-crc.patch
Patch2: 0001-modify-xml2-config-and-pkgconfig-behaviour.patch
Patch3: 0002-Fix-an-error-in-xmlCleanupParser.patch
Patch4: 0003-Fix-missing-break-on-last-function-for-attributes.patch
Patch5: 0004-xmllint-memory-should-fail-on-empty-files.patch
Patch6: 0005-properly-quote-the-namespace-uris-written-out-during.patch
Patch7: 0006-Fix-a-parsing-bug-on-non-ascii-element-and-CR-LF-usa.patch
Patch8: 0007-Fix-XPath-optimization-with-predicates.patch
Patch9: CVE-2014-0191.patch
Patch10: lp1321869.patch
Patch11: CVE-2014-3660.patch
BuildRequires: python python-devel zlib-devel pkgconfig libxml2-python-build
URL: http://xmlsoft.org/

%description
The libxml2-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxml2 library to manipulate XML files.



%prep
%setup -q -n libxml2-%{version}

# libxml2-2.9.0-do-not-check-crc.patch
%patch1 -p1
# 0001-modify-xml2-config-and-pkgconfig-behaviour.patch
%patch2 -p1
# 0002-Fix-an-error-in-xmlCleanupParser.patch
%patch3 -p1
# 0003-Fix-missing-break-on-last-function-for-attributes.patch
%patch4 -p1
# 0004-xmllint-memory-should-fail-on-empty-files.patch
%patch5 -p1
# 0005-properly-quote-the-namespace-uris-written-out-during.patch
%patch6 -p1
# 0006-Fix-a-parsing-bug-on-non-ascii-element-and-CR-LF-usa.patch
%patch7 -p1
# 0007-Fix-XPath-optimization-with-predicates.patch
%patch8 -p1
# CVE-2014-0191.patch
%patch9 -p1
# lp1321869.patch
%patch10 -p1
# CVE-2014-3660.patch
%patch11 -p1

%build
%configure
# use libxml2 as built by libxml2 source package
mkdir .libs
cp -v %{_libdir}/libxml2.la .
make -C python

%install
rm -fr %{buildroot}
make -C python install \
    DESTDIR=$RPM_BUILD_ROOT \
    pythondir=%{py_sitedir} \
    PYTHON_SITE_PACKAGES=%{py_sitedir}
# Unwanted doc stuff
rm -fr $RPM_BUILD_ROOT%{_datadir}/doc
rm -f python/tests/Makefile*
rm -f $RPM_BUILD_ROOT%{py_sitedir}/*.{la,a}

%clean

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-, root, root)
%doc python/TODO
%doc python/libxml2class.txt
%{py_sitedir}/*


