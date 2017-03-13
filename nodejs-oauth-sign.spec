%{?scl:%scl_package nodejs-oauth-sign}
%{!?scl:%global pkg_name %{name}}
%global enable_tests 0
%{?nodejs_find_provides_and_requires}

Name:       %{?scl_prefix}nodejs-oauth-sign
Version:    0.8.1
Release:    1%{?dist}
Summary:    OAuth1 signing for Node.js
# Apache 2.0 License added upstream, will appear in next release
# https://github.com/mikeal/oauth-sign/blob/master/LICENSE
License:    ASL 2.0
URL:        https://github.com/mikeal/oauth-sign
Source0:    http://registry.npmjs.org/oauth-sign/-/oauth-sign-%{version}.tgz
BuildArch:  noarch
ExclusiveArch: %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{enable_tests}
BuildRequires:    %{?scl_prefix}npm(
%endif

%description
%{summary}.

%prep
%setup -q -n package

%build
#nothing to do

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/oauth-sign
cp -pr index.js package.json %{buildroot}%{nodejs_sitelib}/oauth-sign

%nodejs_symlink_deps

%if 0%{enable_tests}
%check
%nodejs_symlink_deps --check

%endif

#test requires network
#%%check
#%%{__nodejs} test.js

%files
%{nodejs_sitelib}/oauth-sign
%doc README.md LICENSE

%changelog
* Wed Sep 07 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.8.1-1
- Updated with script

* Thu Jun 09 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.0-4
- Resolves: rhbz#1334856 , fixes wrong license

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.3.0-3
- rebuilt

* Thu Oct 17 2013 Tomas Hrcka <thrcka@redhat.com> - 0.3.0-2
- replace provides and requires with macro

* Sun Jun 23 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.3.0-1
- new upstream release 0.3.0

* Sat Jun 22 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-3
- restrict to compatible arches

* Mon Apr 15 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-2
- add macro for EPEL6 dependency generation

* Fri Apr 12 2013 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.2.0-2
- Add support for software collections

* Fri Apr 05 2013 T.C. Hollingsworth <tchollingsworth@gmail.com> - 0.2.0-1
- initial package
