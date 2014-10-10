%define upstream_name    Log-Dispatch-Array
%define upstream_version 1.003

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Log events to an array (reference)
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Log/Log-Dispatch-Array-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(Log::Dispatch::Output)
BuildRequires:	perl(Test::Deep)
BuildArch:	noarch

%description
This provides a Log::Dispatch log output system that appends logged events
to an array reference. This is probably only useful for testing the logging
of your code.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes LICENSE META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.1.0-2mdv2011.0
+ Revision: 655042
- rebuild for updated spec-helper

* Thu Mar 04 2010 Jérôme Quelin <jquelin@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 514099
- import perl-Log-Dispatch-Array


* Thu Mar 04 2010 cpan2dist 1.001-1mdv
- initial mdv release, generated with cpan2dist


