Name:          uom-lib
Version:       1.0.1
Release:       6%{?dist}
Summary:       Java Unit of Measurement Libraries (JSR 363)
License:       BSD
URL:           https://github.com/unitsofmeasurement/%{name}
Source0:       https://github.com/unitsofmeasurement/%{name}/archive/%{version}/%{name}-%{version}.tar.gz
Patch1:        javadoc-build-failures.patch

BuildRequires: junit
BuildRequires: maven-local
BuildRequires: maven-jar-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-dependency-plugin
BuildRequires: maven-source-plugin
BuildRequires: mvn(org.apache.felix:maven-bundle-plugin)
BuildRequires: mvn(tec.uom:uom-parent:pom:)
BuildRequires: mvn(javax.measure:unit-api)

BuildArch:     noarch

%description
Units of Measurement Libraries - extending and complementing JSR 363.

%package common
Summary:       Java Units of Measurement Common Library

%description common
Units of Measurement Common Library - extending and complementing JSR 363.

%package javadoc
BuildArch:     noarch
Summary:       Javadoc for the Units of Measurement Libraries

%description javadoc
This package contains documentation for the Units of Measurement
Libraries (JSR 363).

%prep
%setup -q -n %{name}-%{version}
%patch1 -p1

%pom_remove_plugin :maven-javadoc-plugin common/pom.xml

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%doc README.md
%license LICENSE.txt

%files javadoc -f .mfiles-javadoc

%changelog
* Fri Apr 07 2017 Nathan Scott <nathans@redhat.com> - 1.0.1-6
- Rebuilt with a Java 8 buildroot.

* Wed Apr 05 2017 Nathan Scott <nathans@redhat.com> - 1.0.1-5
- Spec file changes for building on RHEL7.

* Wed Mar 22 2017 Nathan Scott <nathans@redhat.com> - 1.0.1-4
- Incorprate feedback from gil cattaneo on all uom packages.

* Tue Feb 28 2017 Nathan Scott <nathans@redhat.com> - 1.0.1-3
- Resolve lintian errors - source, license, documentation.

* Fri Feb 24 2017 Nathan Scott <nathans@redhat.com> - 1.0.1-2
- Add unitsofmeasurement prefix to package name.

* Thu Oct 13 2016 Nathan Scott <nathans@redhat.com> - 1.0.1-1
- Initial version.
