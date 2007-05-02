%define module	Tree-Trie
%define name	perl-%{module}
%define version 1.3
%define release %mkrel 1

Name:		    %{name}
Version:	    %{version}
Release:	    %{release}
Summary:	    A data structure optimized for prefix lookup
License:	    GPL
Group:		    Development/Perl
URL:		    http://search.cpan.org/dist/%{module}
Source:		    http://www.cpan.org/modules/by-module/Tree/%{module}-%{version}.tar.bz2
%if %{mdkversion} < 1010
BuildRequires:	perl-devel
%endif
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Test::Pod::Coverage)
BuildArch:	    noarch
BuildRoot:	    %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
%{__make} test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/Tree
%{_mandir}/*/*

