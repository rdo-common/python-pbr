%global pypi_name pbr

Name:           python-%{pypi_name}
Version:        0.5.11
Release:        2%{?dist}
Summary:        Python Build Reasonableness

License:        ASL 2.0
URL:            http://pypi.python.org/pypi/pbr
Source0:        http://pypi.python.org/packages/source/p/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
BuildArch:      noarch
 
BuildRequires:  python2-devel
# very new required, when also using tests
#BuildRequires:  python-d2to1 >= 0.2.10
BuildRequires:  python-d2to1
BuildRequires:  python-sphinx
# not necessary, but listed in requirements.txt
# Requires:       python-setuptools_git
# BuildRequires:  python-setuptools_git
BuildRequires:  python-testtools
#BuildRequires:  python-testscenarios
#BuildRequires:  python-testresources
# not in the repos, yet
#BuildRequires:  python-discover
# BuildRequires:  python-coverage >= 3.6
#BuildRequires:  python-flake8
# BuildRequires:  python-mox
# not in the repos, yet
#BuildRequires:  python-testrepository
# BuildRequires:  python-subunit

%description
PBR is a library that injects some useful and sensible default behaviors into 
your setuptools run. It started off life as the chunks of code that were copied
between all of the OpenStack projects. Around the time that OpenStack hit 18 
different projects each with at least 3 active branches, it seems like a good 
time to make that code into a proper re-usable library.

%prep
%setup -q -n %{pypi_name}-%{version}

# remove unused requirement
sed -i '/setuptools_git/d' requirements.txt
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info


%build
%{__python} setup.py build

# generate html docs 
sphinx-build doc/source html
# remove the sphinx-build leftovers
rm -rf html/.{doctrees,buildinfo}


%install
%{__python} setup.py install --skip-build --root %{buildroot}

%check
# we don't have the necessary br's, yet
#%{__python} setup.py test

%files
%doc html README.rst LICENSE
%{python_sitelib}/%{pypi_name}-%{version}-py?.?.egg-info
%{python_sitelib}/%{pypi_name}

%changelog
* Fri May 31 2013 Matthias Runge <mrunge@redhat.com> - 0.5.11-2
- remove requirement setuptools_git

* Fri May 17 2013 Matthias Runge <mrunge@redhat.com> - 0.5.11-1
- update to 0.5.11 (rhbz#962132)
- disable tests, as requirements can not be fulfilled right now

* Thu Apr 25 2013 Matthias Runge <mrunge@redhat.com> - 0.5.8-1
- Initial package.
