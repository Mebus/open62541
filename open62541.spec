Name:     open62541
Version:  1.1.2
Release:  1%{?dist}
Summary:  OPC UA implementation
License:  MPLv2.0
URL:      http://open62541.org
Source0:  https://github.com/open62541/open62541/archive/v%{version}.tar.gz

BuildRequires: cmake3, python

%description
open62541 is a C-based library (linking with C++ projects is possible)
with all necessary tools to implement dedicated OPC UA clients and servers,
or to integrate OPC UA-based communication into existing applications.

%package  devel
Summary:  Development files for %{name}
Requires: %{name}%{?_isa} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{name}-%{version}

%build
%cmake3 -DUA_ENABLE_AMALGAMATION=ON .
make

%install
%make_install

# Remove this from the examples installation
rm examples/CMakeLists.txt

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license LICENSE
%doc AUTHORS CHANGELOG README.md
%{_libdir}/libopen62541.so.*

%files devel
%license LICENSE LICENSE-CC0
%{_libdir}/libopen62541.so
%{_libdir}/pkgconfig/open62541.pc
%dir %{_datadir}/open62541/tools/
%{_datadir}/open62541/tools/*
%{_libdir}/cmake/open62541*
%dir %{_exec_prefix}/share/open62541
%{_includedir}/open62541.h

%doc FEATURES.md
%doc examples/

%changelog
* Fri Sep 25 2020 Mebus <mebus@mailaix.de> - 1.1.2-1
- New version of open62541
- Fix spec file
* Tue Sep 05 2017 Jens Reimann <jreimann@redhat.com> - 0.3-1
- New version of open62541
- Adapt for cmake3
* Thu Aug 31 2017 Jens Reimann <jreimann@redhat.com> - 0.2-1
- Initial version of the package

