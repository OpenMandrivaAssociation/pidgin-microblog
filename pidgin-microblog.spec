%define upstream_name mbpurple

Name:           pidgin-microblog
Version:        0.2.1
Release:        %mkrel 2
Summary:        Libpurple plug-in supporting microblog services like Twitter
Group:          Networking/Instant messaging
License:        GPLv3+
URL:            http://code.google.com/p/microblog-purple/
Source0: http://microblog-purple.googlecode.com/files/%{upstream_name}-%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-buildroot

BuildRequires:  pidgin-devel >= 2.5, ElectricFence

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
export CFLAGS="$RPM_OPT_FLAGS"
make LIBDIR=%{_libdir}

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT LIBDIR=%{_libdir}
chmod 0755 $RPM_BUILD_ROOT%{_libdir}/purple-2/libtwitter.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc COPYING README.txt
%{_libdir}/purple-2/*.so
%{_datadir}/pixmaps/pidgin/protocols/*/twitter.png
%{_datadir}/pixmaps/pidgin/protocols/*/identica.png
%{_datadir}/pixmaps/pidgin/protocols/*/laconica.png
