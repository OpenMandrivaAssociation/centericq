%define name centericq
%define version 4.21.0
%define release %mkrel 7

Version:	%{version}
Summary:	Console ncurses based ICQ2000, Yahoo!, MSN, AIM, IRC client
Name:		%{name}
Release:	%{release}
License:	GPL
Group:		Networking/Instant messaging
Source:		http://konst.org.ua/download/%{name}-%{version}.tar.bz2
Patch:      centericq-4.21.0-x86_64.diff
URL:		http://konst.org.ua/centericq/
Buildrequires:	ncurses-devel
BuildRequires:	openssl-devel
BuildRequires:	libstdc++-devel
BuildRequires:	glib-devel
BuildRequires:	curl-devel
BuildRequires:	jpeg-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
centericq is a text mode menu- and window-driven IM interface. Currently
ICQ2000, Yahoo!, MSN, AIM TOC and IRC protocols are supported. It allows
you to send, receive, and forward messages, URLs and, SMSes, mass
message send, search for users (including extended "whitepages search"),
view users' details, maintain your contact list directly from the
program (including non-icq contacts), view the messages history,
register a new UIN and update your details, be informed on receiving
email messages, automatically set away after the defined period of
inactivity (on any console), and have your own ignore, visible and
invisible lists. It can also associate events with sounds, has support
for Hebrew and Arabic languages and allows to arrange contacts into
groups.

%prep 

%setup -q
%patch -p0
%build
# solve segfaults
./configure

%install

rm -rf $RPM_BUILD_ROOT
%makeinstall

#rm $RPM_BUILD_ROOT/%_datadir/locale/locale.alias
rm -Rf $RPM_BUILD_ROOT/%_includedir/

%find_lang %name

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %name.lang
%defattr (-,root,root)
%doc README COPYING INSTALL TODO ChangeLog ABOUT-NLS AUTHORS NEWS
%{_bindir}/*
%_mandir/man1/*
%_datadir/%name


