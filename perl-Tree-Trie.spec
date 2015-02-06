%define upstream_name	 Tree-Trie
%define upstream_version 1.9

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.9
Release:	3

Summary:	A data structure optimized for prefix lookup
License:	GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Tree/Tree-Trie-1.9.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)

BuildArch:	noarch

%description
This module implements a trie data structure.  The term "trie"
comes from the word retrieval, but is generally pronounced like
"try".  A trie is a tree structure (or directed acyclic graph),
the nodes of which represent letters in a word.  For example, the
final lookup for the word 'bob' would look something like
"$ref->{'b'}{'o'}{'b'}{HASH(0x80c6bbc)}" (the HASH being an end
marker).  Only nodes which would represent words in the trie
exist, making the structure slightly smaller than a hash of the
same data set.

The advantages of the trie over other data storage methods is that lookup times
are O(1) WRT the size of the index. For sparse data sets, it is probably not as
efficient as performing a binary search on a sorted list, and for small files,
it has a lot of overhead.  The main advantage (at least from my perspective) is
that it provides a relatively cheap method for finding a list of words in a
large, dense data set which begin with a certain string.

As of version 0.3 of this module, the term "word" in this documentation can
refer to one of two things: either a refeence to an array of strings, or a
scalar which is not an array ref.  In the case of the former, each element of
the array is treated as a "letter" of the "word".  In the case of the latter,
the scalar is evaluated in string context and it is split into its component
letters.  Return values of methods match the values of what is passed in --
that is, if you call lookup() with an array reference, the return value will be
an array reference (if appropriate).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm -f t/02_pod_cover.t

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/Tree
%{_mandir}/*/*


%changelog
* Mon May 09 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.800.0-1mdv2011.0
+ Revision: 672881
- update to new version 1.8

* Sat Nov 06 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.700.0-1mdv2011.0
+ Revision: 594310
- update to new version 1.7

* Tue Jul 13 2010 Jérôme Quelin <jquelin@mandriva.org> 1.600.0-1mdv2011.0
+ Revision: 552692
- update to 1.6

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 1.500.0-1mdv2010.0
+ Revision: 437260
- rebuild using %%perl_convert_version

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Oden Eriksson <oeriksson@mandriva.com>
    - nuke borked tests

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Aug 22 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.5-1mdv2008.0
+ Revision: 69251
- update to new version 1.5

* Wed May 02 2007 Olivier Thauvin <nanardon@mandriva.org> 1.3-1mdv2008.0
+ Revision: 20768
- 1.3


* Thu Aug 31 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-2mdv2007.0
- buildrequires perl(Test::Pod)

* Mon Jul 10 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.2-1mdv2007.0
- New version 1.2

* Thu Oct 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-3mdk
- oops, fixed descript line length

* Thu Oct 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.1-2mdk
- %%mkrel
- spec cleanup
- fix directory ownership
- test in %%check
- better summary
- reformat description

* Thu Jul 14 2005 Oden Eriksson <oeriksson@mandriva.com> 1.1-1mdk
- initial Mandriva package


