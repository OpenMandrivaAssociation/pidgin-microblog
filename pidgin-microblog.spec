%define upstream_name mbpurple
%define _disable_ld_no_undefined 1

Name:           pidgin-microblog
Version:        0.3.0
Release:        %mkrel 1
Summary:        Libpurple plug-in supporting microblog services like Twitter
Group:          Networking/Instant messaging
License:        GPLv3+
URL:            http://code.google.com/p/microblog-purple/
Source0: http://microblog-purple.googlecode.com/files/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  pidgin-devel >= 2.5

%description
The project aims is to develop a set of microblog support in LibPurple base
client like Pidgin. Currently it only support Twitter through the conversation
windows.

Currently the source can be built and run on Windows Vista and Ubuntu 8.04.1.
Other platform with LibPurple should works, but we don't have time (yet) to
test it.

%prep
%setup -q -n %{upstream_name}-%{version}

%build
export CFLAGS="%optflags"
make LIBDIR=%{_libdir} LDFLAGS="%{ldflags}"

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc README.txt
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/*.png
%{_datadir}/purple/ca-certs/EquifaxSecureGlobaleBusinessCA.pem


%changelog
* Sat Nov 27 2010 Funda Wang <fwang@mandriva.org> 0.3.0-1mdv2011.0
+ Revision: 601763
- new version 0.3.0

* Sun Dec 27 2009 Frederik Himpe <fhimpe@mandriva.org> 0.2.4-1mdv2010.1
+ Revision: 482736
- Update to new version 0.2.4
- Don't package GPLv3 COPYING

* Tue Sep 01 2009 Eugeni Dodonov <eugeni@mandriva.com> 0.2.2-2mdv2010.0
+ Revision: 423128
- Updated to 0.2.2

* Sat Mar 07 2009 Jérôme Soyer <saispo@mandriva.org> 0.2.1-2mdv2009.1
+ Revision: 351481
- Change BR

* Fri Mar 06 2009 Jérôme Soyer <saispo@mandriva.org> 0.2.1-1mdv2009.1
+ Revision: 349786
- Fix RPM Group
- import pidgin-microblog


