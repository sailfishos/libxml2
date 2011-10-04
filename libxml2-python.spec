Summary: Python bindings for the libxml2 library
Name: libxml2-python
Version: 2.7.8
Release: 1 
License: MIT
Group: System/Libraries
Source: ftp://xmlsoft.org/libxml2/libxml2-%{version}.tar.gz
BuildRequires: python python-devel zlib-devel pkgconfig libxml2-python-build
URL: http://xmlsoft.org/

%description
The libxml2-python package contains a module that permits applications
written in the Python programming language to use the interface
supplied by the libxml2 library to manipulate XML files.



%prep
%setup -q -n libxml2-%{version}

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


