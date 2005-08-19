Summary: SME Server qpsmtpd module
%define name smeserver-qpsmtpd
Name: %{name}
%define version 1.0.0
%define release 01
Version: %{version}
Release: %{release}
License: GPL
Vendor: SME Server developers
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Packager: Gordon Rowell <gordonr@gormand.com.au>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: qpsmtpd daemontools
Requires: qpsmtpd-plugins
Requires: smeserver-qpsmtpd-tnef2mime
Requires: ipsvd
Requires: smeserver-clamav
Requires: e-smith-spamassassin
Requires: e-smith-lib >= 1.15.1-33
Obsoletes: e-smith-obtuse-smtpd
Obsoletes: e-smith-qmail-smtpd
Obsoletes: e-smith-mailfront
Obsoletes: e-smith-ssl-mailfront
Provides: e-smith-smtpd
Obsoletes: e-smith-qpsmtpd
Provides: e-smith-qpsmtpd
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
AutoReqProv: no

%description
SME Server qpsmtpd smtpd module

%changelog
* Fri Aug 19 2005 Gordon Rowell <gordonr@gormand.com.au>
- [1.0.0-01]
- Package renamed to smeserver-qpsmtpd

* Thu Aug 18 2005 Shad L. Lords <slords@mail.com>
- [0.0.4-27sme01]
- Change e-smith-clamav to smeserver-clamav

* Thu Aug 18 2005 Gordon Rowell <gordonr@gormand.com.au>
- [0.0.4-27]
- Expand goodrcptto in domain-* events [SF: 1257199]

* Tue Aug 16 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-26]
- Fix uid/gid which sslio wrapper runs as for sqpsmtpd. [SF: 1257284]
- Add Requires headers for e-smith-clamav and e-smith-spamassassin.

* Mon Aug 15 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-25]
- Change name of plugins RPM in Requires: header. [SF: 1242326]

* Wed Jul 27 2005 Gordon Rowell <gordonr@gormand.com.au>
- [0.0.4-24]
- Enabled check_basicheaders, requiring a From and Date header.
- Configure db default smtpd{MaxDateOffset}==0. Set it to a non-zero
  value (e.g. 366) to reject mail with silly dates.
  [SF: 1244977]

* Tue Jul 19 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-23]
- Remove explicit pathnames in db opens. [SF: 1216546 (Shad)]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-22]
- Fix metadata OUTPUT_PATH to OUTPUT_FILENAME [SF: 1237193]

* Mon Jul 18 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-21]
- Fix up db default qpsmtpd{tnef2mime} -> smtpd{tnef2mime} so it is
  actually enabled by default [SF:1227668 (Shad)]

* Wed Jul 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-20]
- Fix errors in SSL PEM file template expansion [SF: 1237193]

* Tue Jul 12 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-19]
- Added Michael Weinberger's smeserver-qpsmtpd-tnef2mime - [SF:1227668]
- Added config db defaults to enable plugin

* Thu Jun 16 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-18]
- Remove bogus /var/service/qpsmtpd/peers/{0,local}
  directories (this time for sure, Rocky!) [SF: 1210727]

* Tue Jun 14 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-17]
- Small patch from Gordon to fix cvs interaction.

* Mon Jun 13 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-16]
- Add Obsoletes header for e-smith-ssl-mailfront. [SF: 1219069]

* Sun Jun 12 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-15]
- Remove bogus /var/service/qpsmtpd/peers/{0,local}
  directories, and fix typo. [SF: 1210727]

* Tue May 31 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-14]
- Fix location of templates-begin files. [SF: 1210727]

* Tue May 24 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-13]
- Add "access" default property for qpsmtpd and sqpsmtpd services.
  [SF: 1205847]
- Make sure that empty templates-begin files exist in peers/{0,local}
  templates directories.

* Thu May 11 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.4-12]
- Fix up config/relayclients - need a dot after network blocks

* Thu May 11 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.4-11]
- Also regenerate goodrcptto in {user,pseudonym}-modify, since
  details about the account may have changed

* Thu May 11 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.4-10]
- Actually regenerate goodrcptto in the events mentioned in
  0.0.3-01 (typo in createlinks)

* Fri May 06 2005 Charlie Brady <charlieb@e-smith.com>
- [0.0.4-09]
- Add type and status defaults for qpsmtpd and sqpsmtpd services.

* Wed May 4 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-08
- Fixed up SMTP Authentication status mismatch

* Wed May 4 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-07
- Clean up configuration, using "runenv" file for each service
- Check various properties to determine whether to enable plugins

* Wed May 4 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-06
- Move mailpatterns defaults to e-smith-email

* Wed May 4 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-05
- New arguments to auth_cvm_unix_local to allow AUTH to be 
  enabled/disabled for smtp or ssmtp:
  enable_smtp no enable_ssmtpd yes
- Checks config db defaults for [s]smtpd{Authentication}

* Wed May 4 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-04
- Remove spurious return statement

* Wed May 4 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-03
- Fix auth_cvm_unix_local to actually check with CVM
- TODO: auth-cram-md5 and auth-local (?)

* Sat Apr 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-02
- Check for relayclient in check_badrcptto_patterns
- Actually check that the user exists in the prototype auth module

* Sat Apr 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.4-01
- Added Provides: e-smith-smtpd to ease migration from e-smith-mailfront

* Sat Apr 30 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.3-04
- Move badrcpto_patterns into a configuration file
- Updated comment blocks in plugins
- Parameterised a number of qpsmtpd config files
- TODO: Database defaults, finalise parameterisation

* Fri Apr 29 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.3-03
- Renamed auth module to auth_cvm_unix_local

* Fri Apr 29 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.3-02
- Added auth_cvm-unix-local for AUTH LOGIN and AUTH PLAIN
- TODO: Actually check with CVM - currently uses colon separated
  plain text config/flat_auth_pw

* Fri Apr 29 2005 Gordon Rowell <gordonr@gormand.com.au> 0.0.3-01
- Regenerate goodrcptto in {user,pseudonym}-{create,delete} 
  - thanks Paul Nesbit
- Split qpsmtpd-plugins-openfusion into separate RPM
- Note: mailer-daemon now works due to change I suggested in 
  check_goodrcptto: match on full string, then match again on
  string with extension stripped - thanks Gavin Carr
- Unset RELAYCLIENT in check_norelay (probably not required)

* Tue Apr 26 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.2-03]
- Pass correct parameter to check_goodrcptto
- TODO: mailer-daemon is currently being denied due to goodrcptto 
  extension folding

* Tue Apr 26 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.2-02]
- Added plugins/check_badrcptto_patterns to check for bang, shriek
  and double at paths.
- Added plugins/check_norelay to allow specific hosts to be denied relaying

* Tue Apr 26 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.2-01]
- Added plugins/virus/patterns_filter, based on Gavin Carr's exe_filter,
  but without the dependency on Email::MIME. This is a simple-minded 
  filter, which doesn't care about MIME boundaries (as per the 
  mailfront version).

* Mon Apr 25 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.1-03]
- Fixed path to clamav socket in 80clamdscan (currently unused)
- Parameterised many of the templates
- TODO: Need to parameterise rshbl
- Added a set of qpsmtpd plugins from Gavin Carr of OpenFusion:
        http://www.openfusion.com.au/labs/qpsmtpd/
- TODO: Need norelayclient setting (to deny relay from router)
- TODO: sqpsmtpd needs testing - fails with (maybe just from stunnel client)
  "421 See http://smtpd.develooper.com/barelf.html"

* Thu Apr 21 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.1-02]
- Initial cut of sqpsmtpd

* Thu Apr 21 2005 Gordon Rowell <gordonr@gormand.com.au> 
- [0.0.1-01]
- Initial packaging

%prep
%setup

%build
perl createlinks

mkdir -p root/service
mkdir -p root/var/spool/qpsmtpd

for service in qpsmtpd sqpsmtpd
do
    ln -s /var/service/$service 	root/service/$service

    mkdir -p 				root/var/service/$service/supervise
    touch 				root/var/service/$service/down
    mkdir -p 				root/var/service/$service/log/supervise
    mkdir -p 				root/var/log/$service

    ln -s /usr/lib/qpsmtpd/lib		root/var/service/$service/
    ln -s /usr/lib/qpsmtpd/plugins	root/var/service/$service/
    ln -s /usr/bin/qpsmtpd		root/var/service/$service/
    ln -s /usr/bin/qpsmtpd-forkserver	root/var/service/$service/
done

for dir in env peers ssl config
do
    mkdir -p 				root/var/service/qpsmtpd/$dir
    ln -s ../qpsmtpd/$dir 		root/var/service/sqpsmtpd/$dir
done
mkdir -p root/var/service/qpsmtpd/peers/
mkdir -p root/etc/e-smith/templates/var/service/qpsmtpd/peers/{0,local}
touch root/etc/e-smith/templates/var/service/qpsmtpd/peers/{0,local}/template-begin

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/qpsmtpd "attr(1755,root,root)" \
    --file /var/service/qpsmtpd/down "attr(0644,root,root)" \
    --file /var/service/qpsmtpd/run "attr(0755,root,root)" \
    --dir /var/service/qpsmtpd/supervise "attr(0700,root,root)" \
    --dir /var/service/qpsmtpd/env "attr(0755,root,root)" \
    --file /var/service/qpsmtpd/env/PATH "attr(0644,root,root)" \
    --dir /var/service/qpsmtpd/log "attr(1755,root,root)" \
    --file /var/service/qpsmtpd/log/run "attr(0755,root,root)" \
    --dir /var/service/qpsmtpd/log/supervise "attr(0700,root,root)" \
    --dir /var/log/qpsmtpd "attr(2750,smelog,smelog)" \
	\
    --dir /var/service/sqpsmtpd "attr(1755,root,root)" \
    --file /var/service/sqpsmtpd/down "attr(0644,root,root)" \
    --file /var/service/sqpsmtpd/run "attr(0755,root,root)" \
    --dir /var/service/sqpsmtpd/supervise "attr(0700,root,root)" \
    --dir /var/service/sqpsmtpd/env "attr(0755,root,root)" \
    --file /var/service/sqpsmtpd/env/PATH "attr(0644,root,root)" \
    --dir /var/service/sqpsmtpd/log "attr(1755,root,root)" \
    --file /var/service/sqpsmtpd/log/run "attr(0755,root,root)" \
    --dir /var/service/sqpsmtpd/log/supervise "attr(0700,root,root)" \
    --dir /var/log/sqpsmtpd "attr(2750,smelog,smelog)" \
	\
    --file /var/service/sqpsmtpd/sqpsmtpd "attr(0755,root,root)" \
    --dir /var/spool/qpsmtpd "attr(2750,qpsmtpd,clamav)" \
    > %{name}-%{version}-%{release}-filelist

%pre
/sbin/e-smith/create-system-user qpsmtpd 453 \
	'qpsmtpd system user' /var/service/qpsmtpd /bin/false
%post

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
