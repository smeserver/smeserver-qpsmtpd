Summary: SME Server qpsmtpd module
%define name smeserver-qpsmtpd
Name: %{name}
%define version 1.2.1
%define release 06
Version: %{version}
Release: %{release}
License: GPL
Vendor: SME Server developers
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: smeserver-qpsmtpd-1.2.1-LiteralIP.patch
Patch1: smeserver-qpsmtpd-1.2.1-badrcptto-hosts.patch
Patch2: smeserver-qpsmtpd-1.2.1-check_smtp_forward.patch
Packager: Gordon Rowell <gordonr@gormand.com.au>
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: qpsmtpd >= 0.31.1-1sme08
Requires: daemontools
Requires: qpsmtpd-plugins >= 0.0.1-sme04
Requires: ipsvd
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
* Fri Aug 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-06
- Add check_smtp_forward plugin which contacts the internal mail
  server(s) to determine whether the mail would be accepted. If
  so, just let it queue normally 
- TODO: Add configuration to plugins file if required [SME: 1850]

* Fri Aug 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-05
- Revert last change. Enhancing the smtp-forward plugin to handle
  multiple internal mail servers for different domains is too
  complex. Let's let qmail do that work. [SME: 710]

* Fri Aug 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-04
- Re-enable smtp-forward plugin requiring version which declines if
  the connection is from a relayclient, to allow fallthrough to standard
  qmail-queue plugin.
- Add default/failsafe queue/qmail-queue plugin [SME: 710]

* Thu Jul 27 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-03
- Remove hosts from badrcptto - we only handle domains [SME: 1777]

* Sat Jul 1 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-02
- Allow mail to [$ExternalIP] to support postmaster@[$ExternalIP] [SME: 1675]

* Sat Jul 1 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-01
- Roll tarball with patches to 1.2.0-10

* Thu Jun 29 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-10
- Change default smtpgreeting to $SystemName.$DomainName [SME: 1325]

* Thu Jun 29 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-09
- Template /var/service/qpsmtpd/config/smtpgreeting, defaulting to 
  $DomainName. To set a custom greeting, set $smtpd{Greeting} [SME: 1325]

* Mon Jun 26 2006 Filippo Carletti <carletti@mobilia.it> 1.2.0-08
- Expand badrcptto on group create/modifiy/delete events [SME: 1632]

* Wed Jun 21 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-07
- Remove configuration for klez_filter scanner as it duplicates
  work of the pattern_filter [SME: 1620]

* Tue Jun 20 2006 Filippo Carletti <carletti@mobilia.it> 1.2.0-06
- Expand goodrcptto on group create/modifiy/delete events [SME: 1616]

* Mon Jun 5 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-05
- Improve peformance of pattern_filter plugin [SME: 1532]
- TODO: Remove obsolete code and comments from that plugin

* Wed May 17 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.0-04
- Allow all mail for domains which are being forwarded to internal
  mail servers [SME: 1253]

* Thu Apr 6 2006 Gavin Weight <gweight@gmail.com> 1.2.0-03
- Revert back to loglevel 8 from 6. [SME: 503]

* Thu Mar 23 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.0-02
- Disable use of smtp-forward plugin (probably temporarily) in
  DelegateMailServer mode, to avoid mail looping problem. Always
  use qmail-queue plugin (for now). [SME: 1121]

* Wed Mar 15 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.0-01
- Roll stable stream version. [SME: 1016]

* Fri Feb 17 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.2-04
- Exempt local networks from dnsbl lookup. [SME: 830]

* Fri Feb 10 2006 <gordonr@gormand.com.au> 1.0.2-03
- Call queue/smtp-forward to connect to DelegateMailServer
  instead of queueing locally when DelegateMailServer is set [SME: 710]

* Mon Feb  6 2006 <charlie_brady@mitel.com> 1.0.2-02
- Enable resolvable_fromhost check by default, and add
  whitelistsenders config for local domains. [SME: 638]

* Sun Feb  5 2006 <charlie_brady@mitel.com> 1.0.2-01
- Roll new tarball. [SME: 651]

* Sun Feb  5 2006 <charlie_brady@mitel.com> 1.0.1-21
- Remove unused patterns.default remnants. Ensure that all
  templates2expand directories are populated only by createlinks
  script. [SME: 651]

* Sat Feb  4 2006 <charlie_brady@mitel.com> 1.0.1-20
- Expand badhelo template during ip-change event, and remove
  bogus expansions /var/qmail/control/badhelo templates. [SME: 651]

* Fri Feb 3 2006 Shad L. Lords <slords@mail.com> 1.0.1-19
- Add missing template-begin file in rhsbl directory [SME: 596]

* Fri Feb  3 2006 <carletti@mobilia.it> 1.0.1-18
- Expand config/relayclients in network-(create|delete) events
  [SME: 649]

* Thu Feb  2 2006 <charlie_brady@mitel.com> 1.0.1-17
- Add template for invalid_resolvable_fromhost configuration file
  [SME: 638]

* Mon Jan 30 2006 Charlie Brady <charlie_brady@mitel.com> 1.0.1-16
- Fix warnings during template expansion, if spamassassin and/or clamd
  is not installed/configured. Remove dependencies on packages which
  are optional. Ensure that clamav group exists before installation.
  Remove one redundant template fragment (which consisted of only comments).
  [SME: 606]

* Sat Jan 28 2006 Shad L. Lords <slords@mail.com> 1.0.1-15
- Add support for rhsbl entries to db [SME: 596]

* Thu Jan 26 2006 Charlie Brady <charlieb@e-smith.com> 1.0.1-14
- Remove remnant mailrules.default templates and template
  expansions. [SME: 454]

* Wed Jan 25 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-13
- Add defaults qpsmtpd{Bcc} == disabled and qpsmtpd{BccUser} == maillog 
- To enable mail logging:
  - Create maillog user
  - config setprop qpsmtpd Bcc enabled 
  - signal-event email-update [SME: 13]

* Wed Jan 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-12
- Really reduce default qpsmtpd{LogLevel} to LOGINFO (6) [SME: 503]

* Wed Jan 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-11
- Reduce default qpsmtpd{LogLevel} to LOGINFO (7) [SME: 503]

* Thu Jan 12 2006 Charlie Brady <charlieb@e-smith.com> 1.0.1-10
- Fix goodrcptto and mailrules templates for single domain
  pseudonym entries. [SME: 368]

* Thu Oct 13 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-09
- Default RequireResolvableFromHost to "no" [SF: 1269382]

* Thu Oct 13 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-08
- SIGHUP [s]qpsmtpd to re-read config in email-update [SF: 1252072]

* Mon Oct 10 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-07
- And finally, the env directory [SF: 1313800]

* Mon Oct 10 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-06
- And the config directory [SF: 1313800]

* Mon Oct 10 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-05
- Need to create ssl directory to allow template expansion [SF: 1313800]

* Fri Oct 7 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-04
- And the path to the runenv directory [SF: 1313800]

* Fri Oct 7 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-03
- And fix up path to config directory [SF: 1313800]

* Fri Oct 7 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-02
- Remove symlinks from sqpsmtpd directory [SF: 1313800]

* Fri Oct 7 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.1-01
- Roll new tarball, including patches to 1.0.0-11

* Fri Oct 7 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-11
- Added missing = to max_size parameter for clamav plugin [SF: 1308976]

* Thu Oct 6 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-10
- Added db defaults for qpsmtpd{LogLevel}=='8' and
  $qpsmtpd{RequireResolvableFromHost}=='yes' [SF: 1314202]

* Thu Sep 22 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-09
- Allow mail to root@domain. If you want to block it,
  db accounts setprop root Visible internal [SF: 1252375]

* Thu Sep 22 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-08
- And pick correct value from clamav entry: [SF: 1245756]
  $qpsmtpd{MaxScannerSize} || $clamav{StreamMaxLength} || "25M";

* Thu Sep 22 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-07
- Configure qpsmtpd{MaxScannerSize}, defaulting to 25MBytes [SF: 1245756]

* Thu Sep 22 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-06
- Set separate softlimit values for data/stack/locked [SF: 1298123]

* Thu Sep 22 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-05
- Set memory_threshold to 1 so that qpsmtpd writes all mail messages
  to disk so that scanners can look at them. Default is 10K [SF: 1298343]

* Mon Aug 29 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-04
- Updated Requires for qpsmtpd to 0.31 [SF: 1231314]
- Change paths to match Peter Holtzer's RPMs - /usr/share/qpsmtpd/
  instead of /usr/lib/qpsmtpd [SF: 1231314]
- Updated Requires for plugins to pick up new paths [SF: 1231314]
- Remove symlinks from /var/service[s]qpsmtpd since they can
  now be done with environment or qpsmtpd config variables [SF: 1231314]
- Remove plugins auth/cvm_unix_local, check_norelay and
  check_badrcptto_patterns which are now in the qpsmtpd tarball [SF: 1231314]

* Mon Aug 29 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-03
- Fix sqpsmtpd script to call sslio with -u and -U args [SF: 1257284]

* Wed Aug 24 2005 Gordon Rowell <gordonr@gormand.com.au> 1.0.0-02
- Configure qpsmtpd{RBLList} with comma separator, but allow 
  either since people are used to colons and we then don't have
  to do a db migration for beta1 -> beta2 [SF: 1267737]

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
%patch0 -p1
%patch1 -p1
%patch2 -p1

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
done

for dir in env config peers ssl
do
    mkdir -p root/var/service/qpsmtpd/$dir
done

mkdir -p root/etc/e-smith/templates/var/service/qpsmtpd/peers/{0,local}
touch root/etc/e-smith/templates/var/service/qpsmtpd/peers/{0,local}/template-begin
touch root/etc/e-smith/templates/var/service/qpsmtpd/config/rhsbl_zones/template-begin

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
/usr/sbin/groupadd -r clamav 2>/dev/null || :
%post

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
