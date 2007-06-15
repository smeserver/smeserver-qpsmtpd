Summary: SME Server qpsmtpd module
%define name smeserver-qpsmtpd
Name: %{name}
%define version 1.2.1
%define release 41
Version: %{version}
Release: %{release}%{?dist}
License: GPL
Group: Networking/Daemons
Source: %{name}-%{version}.tar.gz
Patch0: smeserver-qpsmtpd-1.2.1-LiteralIP.patch
Patch1: smeserver-qpsmtpd-1.2.1-badrcptto-hosts.patch
Patch2: smeserver-qpsmtpd-1.2.1-check_smtp_forward.patch
Patch3: smeserver-qpsmtpd-1.2.1-enable_check_smtp_forward.patch
Patch4: smeserver-qpsmtpd-1.2.1-bcc_mode.patch
Patch5: smeserver-qpsmtpd-1.2.1-peers_plugin.patch
Patch6: smeserver-qpsmtpd-1.2.1-peers_plugin.patch2
Patch7: smeserver-qpsmtpd-1.2.1-usepeers.patch 
Patch8: smeserver-qpsmtpd-1.2.1-usepeers.patch2
Patch9: smeserver-qpsmtpd-1.2.1-rcpthosts_regenerated.patch
Patch10: smeserver-qpsmtpd-1.2.1-mergetnef2mime.patch
Patch11: smeserver-qpsmtpd-1.2.1-usepeers.patch3
Patch12: smeserver-qpsmtpd-1.2.1-usepeers.patch4
Patch13: smeserver-qpsmtpd-1.2.1-control1.patch
Patch14: smeserver-qpsmtpd-1.2.1-control1.patch3
Patch15: smeserver-qpsmtpd-1.2.1-peersinit.patch
Patch16: smeserver-qpsmtpd-1.2.1-rblsbl.patch
Patch17: smeserver-qpsmtpd-1.2.1-peersauth.patch
Patch18: smeserver-qpsmtpd-1.2.1-peersauth.patch2
Patch19: smeserver-qpsmtpd-1.2.1-badmailfrom.patch
Patch20: smeserver-qpsmtpd-1.2.1-nowhitelist.patch
Patch21: smeserver-qpsmtpd-1.2.1-dkim.patch
Patch22: smeserver-qpsmtpd-1.2.1-keeptnef.patch
Patch23: smeserver-qpsmtpd-1.2.1-softlimit.patch
Patch24: smeserver-qpsmtpd-1.2.1-rcpthost.patch
Patch25: smeserver-qpsmtpd-1.2.1-logterse.patch
Patch26: smeserver-qpsmtpd-1.2.1-logterse_stats.patch
Patch27: smeserver-qpsmtpd-1.2.1-qplogsumm.patch
Patch28: smeserver-qpsmtpd-1.2.1-logterse.patch2
Patch29: smeserver-qpsmtpd-1.2.1-qpsmtpd40.patch
Patch30: smeserver-qpsmtpd-1.2.1-qpsmtpd40.patch2
BuildRoot: /var/tmp/%{name}-%{version}-%{release}-buildroot
Requires: qpsmtpd >= 0.40
Requires: perl(Mail::DKIM)
Requires: perl(Mail::DKIM::DkSignature)
Requires: daemontools
Requires: qpsmtpd-plugins >= 0.0.1-sme04
Requires: ipsvd
Requires: e-smith-lib >= 1.16.0-08
Obsoletes: e-smith-obtuse-smtpd
Obsoletes: e-smith-qmail-smtpd
Obsoletes: e-smith-mailfront
Obsoletes: e-smith-ssl-mailfront
Provides: e-smith-smtpd
Obsoletes: e-smith-qpsmtpd
Provides: e-smith-qpsmtpd
Obsoletes: smeserver-qpsmtpd-tnef2mime
Provides: smeserver-qpsmtpd-tnef2mime
Requires: e-smith-base >= 4.15.2
Requires: perl-Convert-TNEF
Requires: perl-IO-stringy
Requires: perl-File-MMagic
Requires: perl-MIME-tools
BuildArchitectures: noarch
BuildRequires: e-smith-devtools
AutoReqProv: no

%description
SME Server qpsmtpd smtpd module

%changelog
* Thu Jun 14 2007 Shad L. Lords <slords@mail.com> 1.2.1-41
- Update for new features in qpsmtpd v0.40

* Thu Jun 14 2007 Shad L. Lords <slords@mail.com> 1.2.1-40
- Remove conflicts qpsmtpd >= 0.33

* Sat Jun 9 2007 Shad L. Lords <slords@mail.com> 1.2.1-39
- Update to correct version of qplogsumm.pl [SME: 2971]

* Fri Jun 08 2007 Shad L. Lords <slords@mail.com> 1.2.1-38
- Add qplogsumm.pl to package for logging [SME: 2971]

* Fri Jun 08 2007 Stephen Noble <support@dungog.net> 1.2.1-37
- Bump

* Fri Jun 08 2007 Stephen Noble <support@dungog.net> 1.2.1-36
- Cumulative statistics for qpsmtpd using logterse [SME: 2971]

* Sun Apr 29 2007 Shad L. Lords <slords@mail.com>
- Clean up spec so package can be built by koji/plague

* Tue Apr 10 2007 Shad L. Lords <slords@mail.com> 1.2.1-35
- Add logterse plugin and reduce logging level [SME: 2875]

* Fri Apr 06 2007 Shad L. Lords <slords@mail.com> 1.2.1-34
- Remove templates2events link for rcpthosts [SME: 2716]

* Wed Mar 07 2007 Shad L. Lords <slords@mail.com> 1.2.1-33
- Add db entry for soft memory limits [SME: 2308]

* Sat Jan 27 2007 Shad L. Lords <slords@mail.com> 1.2.1-32
- Keep TNEF attachment if contains special lookout stuff [SME: 2339]

* Tue Jan 23 2007 Shad L. Lords <slords@mail.com> 1.2.1-31
- Add DomainKey and DKIM signing plugin

* Thu Jan 18 2007 Shad L. Lords <slords@mail.com> 1.2.1-30
- Remove whitelist_soft plugin usage [SME: 2322]

* Sat Jan 13 2007 Shad L. Lords <slords@mail.com> 1.2.1-29
- Rename badmailfrom template to 10sample [SME: 2279]

* Thu Jan 11 2007 Shad L. Lords <slords@mail.com> 1.2.1-28
- Fix peers plugin to hook new methods [SME: 2091]

* Thu Jan 11 2007 Shad L. Lords <slords@mail.com> 1.2.1-27
- Make smtp auth use local plugins [SME: 2091]

* Wed Jan 10 2007 Shad L. Lords <slords@mail.com> 1.2.1-26
- Migrate ordb.org entries away. [SME: 2274]
- Clean-up SBL and RBL lists to use be in the correct place and use
  recognized lists.

* Thu Dec 28 2006 Shad L. Lords <slords@mail.com> 1.2.1-25
- Reverse last change and fix correctly by passing peers/0 to
  the inital peers plugin [SME: 2167]

* Tue Dec 26 2006 Shad L. Lords <slords@mail.com> 1.2.1-24
- Update peers to exit gracefully if no config passed [SME: 2167]

* Thu Dec 07 2006 Shad L. Lords <slords@mail.com>
- Update to new release naming.  No functional changes.
- Make Packager generic

* Fri Dec 1 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-23
- Re-enable these by default for local connections as they already
  check for relayclient() for relevant sections: [SME: 1893]
  30check_badmailfrom
  33check_badrcptto_patterns
  34check_badrcptto
  38check_goodrcptto

* Fri Dec 1 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-22
- Replace config/peers/0 and config/peers/local template directory
  symlinks with a tree of symlinks. Disable the following plugins
  for local connections: [SME: 1893]
  10check_earlytalker
  12count_unrecognized_commands
  16require_resolvable_fromhost
  20rhsbl
  22dnsbl
  30check_badmailfrom
  33check_badrcptto_patterns
  34check_badrcptto
  38check_goodrcptto
  70spamassassin

* Fri Nov 24 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-21
- Fix last change to use SIGUSR1, not SIGHUP, and only for qpsmtpd.
  The peers directories are shared between qpsmtpd and sqpsmtpd [SME: 1893]

* Fri Nov 24 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-20
- Regenerate peers directories in network-{create,delete} [SME: 1893]

* Fri Nov 24 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-19
- Update e-smith-lib requires to pick up configure_peers() change [SME: 1893]
- Add control/1 script and call from run script to configure peers [SME: 1893]

* Wed Nov 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-18
- Ensure config directory resolves for sqpsmtpd service [SME: 1893]

* Wed Nov 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-17
- Create config/peers directory [SME: 1893]

* Wed Nov 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-16
- Expand config/peers/local in the relevant events [SME: 1893]
- TODO: Generate peers links for local networks

* Wed Nov 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-15
- Remove peers/0 templates.metadata file
- Create config/peers templates directories
- Symlink config/peers/{0,local} to ../plugins
- To override local qpsmtpd config, create custom template for
  /var/service/qpsmtpd/config/peers/local [SME: 1893]

* Wed Nov 22 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-14
- Merge in smeserver-qpsmtpd-tnef2mime [SME: 2087]

* Mon Nov 20 2006 Gavin Weight <gweight@gmail.com> 1.2.1-13
- Fix rcpthosts to regenerate on ip-change. [SME: 1926]

* Fri Nov 17 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-12
- Correct last patch (wrong templates.metadata file) [SME: 1893]
- Expand config/peers/0 in the relevant events

* Fri Nov 17 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-11
- Enable Charlie's peers plugin [SME: 1893]
  Use templates.metadata to provide backwards compatibility with 
  add-on template fragments (at least for the first pass)
    config/peers/0 is generated from existing config/plugins template
    config/plugins is now a static file which just loads the peers plugin
- TODO: Generate local plugins file(s) with different config

* Sun Oct 22 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.1-10
- Fix RE used to strip octets from IP address in peers plugin. [SME: 1893]

* Fri Sep 08 2006 Charlie Brady <charlie_brady@mitel.com> 1.2.1-09
- Add 'peers' plugin code. [SME: 1893]

* Thu Aug 24 2006 Filippo Carletti <carletti@mobilia.it> 1.2.1-08
- Add option for stealth mail logging. To enable:
  - config setprop qpsmtpd BccMode bcc [SME: 1876]

* Fri Aug 18 2006 Gordon Rowell <gordonr@gormand.com.au> 1.2.1-07
- Enable check_smtp_forward if any domains are being forwarded
  to internal mail servers [SME: 1850]

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
%patch3 -p1
%patch4 -p1
%patch5 -p1
%patch6 -p1
%patch7 -p1
%patch8 -p1
%patch9 -p1
%patch10 -p1
%patch11 -p1
%patch12 -p1
%patch13 -p1
%patch14 -p1
%patch15 -p1
%patch16 -p1
%patch17 -p1
%patch18 -p1
%patch19 -p1
%patch20 -p1
%patch21 -p1
%patch22 -p1
%patch23 -p1
%patch24 -p1
%patch25 -p1
%patch26 -p1
%patch27 -p1
%patch28 -p1
%patch29 -p1
%patch30 -p1

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

for dir in env config peers ssl config/peers
do
    mkdir -p root/var/service/qpsmtpd/$dir
done

ln -s ../qpsmtpd/config root/var/service/sqpsmtpd/config

mkdir -p root/etc/e-smith/templates/var/service/qpsmtpd/peers/{0,local}
touch root/etc/e-smith/templates/var/service/qpsmtpd/peers/{0,local}/template-begin
touch root/etc/e-smith/templates/var/service/qpsmtpd/config/rhsbl_zones/template-begin

PEERS_CONFIG=root/etc/e-smith/templates/var/service/qpsmtpd/config/peers
mkdir -p $PEERS_CONFIG/0
mkdir -p $PEERS_CONFIG/local

DISABLE_LOCAL="
05auth_cvm_unix_local
10check_earlytalker
12count_unrecognized_commands
16require_resolvable_fromhost
20rhsbl
22dnsbl
70spamassassin
"

for file in $DISABLE_LOCAL
do
    echo "# $file disabled for local connections" > $PEERS_CONFIG/local/$file
done

(
    cd root/etc/e-smith/templates/var/service/qpsmtpd/config/plugins
    for file in *
    do
        [ -e ../peers/0/$file ] || 
            ln -s ../../plugins/$file ../peers/0/$file
        [ -e ../peers/local/$file ] || 
            ln -s ../../plugins/$file ../peers/local/$file
    done
)

%install
rm -rf $RPM_BUILD_ROOT
(cd root   ; find . -depth -print | cpio -dump $RPM_BUILD_ROOT)
rm -f %{name}-%{version}-%{release}-filelist
/sbin/e-smith/genfilelist $RPM_BUILD_ROOT \
    --dir /var/service/qpsmtpd "attr(1755,root,root)" \
    --file /var/service/qpsmtpd/down "attr(0644,root,root)" \
    --file /var/service/qpsmtpd/run "attr(0755,root,root)" \
    --file /var/service/qpsmtpd/control/1 "attr(0755,root,root)" \
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
        \
    --file /usr/local/bin/qplogsumm.pl "attr(0755,root,root)" \
    > %{name}-%{version}-%{release}-filelist

%pre
/sbin/e-smith/create-system-user qpsmtpd 453 \
	'qpsmtpd system user' /var/service/qpsmtpd /bin/false
/usr/sbin/groupadd -r clamav 2>/dev/null || :

TEMPLATES_DIR=/etc/e-smith/templates/var/service/qpsmtpd/config/peers

[ -L $TEMPLATES_DIR/0 ]     && rm -f $TEMPLATES_DIR/0
[ -L $TEMPLATES_DIR/local ] && rm -f $TEMPLATES_DIR/local
true

%post

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}-%{version}-%{release}-filelist
%defattr(-,root,root)
