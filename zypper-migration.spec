#
# spec file for package zypper-migration
#
# Copyright (c) 2015 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

Name:           zypper-migration
Version:        0.1
Release:        0
Requires:       rubygem(%{rb_default_ruby_abi}:suse-connect)
Requires:       zypper >= 1.11.34
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildRequires:  ruby-macros >= 5
BuildRequires:  zypper >= 1.11.34
Source1:        zypper-migration
Summary:        Zypper subcommand for online migration
License:        GPL v2 only
Group:          System/Packages
BuildArch:      noarch

%description
.

%prep

%build

%install
mkdir -p $RPM_BUILD_ROOT/usr/lib/zypper/commands
install -m 755 %{S:1} $RPM_BUILD_ROOT/usr/lib/zypper/commands/

%files
%defattr(-,root,root,-)
/usr/lib/zypper/commands


%changelog
