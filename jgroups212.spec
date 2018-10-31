%{?_javapackages_macros:%_javapackages_macros}
Name:     jgroups212
Version:  2.12.3
Release:  9.3
Summary:  A toolkit for reliable multicast communication
Group:	  Development/Java

License:  LGPLv2
URL:      http://www.jgroups.org
# git clone git://github.com/belaban/JGroups.git
# cd JGroups && git checkout Branch_JGroups_2_12 && git checkout-index -f -a --prefix=jgroups212-2.12.3.Final
# find jgroups212-2.12.3.Final/ -name '*.jar' -type f -delete
# tar -cJf jgroups212-2.12.3.Final.tar.xz jgroups212-2.12.3.Final
Source0:  %{name}-%{version}.Final.tar.xz
Patch0:   %{name}-groupid.patch
BuildArch:     noarch

BuildRequires: maven-local
BuildRequires: maven-compiler-plugin
BuildRequires: maven-install-plugin
BuildRequires: maven-jar-plugin
BuildRequires: maven-javadoc-plugin
BuildRequires: maven-release-plugin
BuildRequires: maven-resources-plugin
BuildRequires: maven-surefire-plugin
BuildRequires: maven-surefire-provider-junit
BuildRequires: bsh
BuildRequires: log4j

Requires:      jpackage-utils
Requires:      java
Requires:      bsh
Requires:      log4j

%description
A toolkit for reliable multicast communication.
It allows developers to create reliable multipoint (multicast) applications
where reliability is a deployment issue, and does not have to be implemented
by the application developer. This saves application developers significant
amounts of time, and allows for the application to be deployed in different
environments, without having to change code.

%package javadoc
Summary:    Javadoc for %{name}

Requires:   jpackage-utils

%description javadoc
%{summary}.

%prep
%setup -q -n %{name}-%{version}.Final
find . -name \*.jar -exec rm -f {} \;

%patch0 -p1

%build
%mvn_build -f

%install
%mvn_install

# Fix incorrect permissions on documentation
chmod 644 README

%files -f .mfiles
%doc LICENSE README INSTALL.html

%files javadoc -f .mfiles-javadoc
%doc LICENSE

%changelog
* Sun Aug 11 2013 Matt Spaulding <mspaulding06@gmail.com> - 2.12.3-7
- Add BR for maven-install-plugin

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2.12.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2.12.3-4
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Thu Aug 23 2012 Matt Spaulding <mspaulding06@gmail.com> - 2.12.3-3
- Changed groupid to org.jgroup212 to fix conflict with jgroup 3
- Now building with UTF-8 source encoding

* Sun Aug 05 2012 Matt Spaulding <mspaulding06@gmail.com> - 2.12.3-2
- Included license in javadoc subpackage
- Corrected license type
- Added missing Requires and BR
- Removed unnecessary define

* Fri Jul 27 2012 Matt Spaulding <mspaulding06@gmail.com> - 2.12.3-1
- Initial package

