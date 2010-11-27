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
