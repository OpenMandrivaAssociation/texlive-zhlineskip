Name:		texlive-zhlineskip
Version:	51142
Release:	2
Summary:	Line spacing for CJK documents
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/zhlineskip
License:	lppl1.3c
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlineskip.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/zhlineskip.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package supports typesetting CJK documents. It allows
users to specify the two ratios between the leading and the
font size of the body text and the footnote text. For CJK
typesetting, these ratios usually range from 1.5 to 1.67. This
package is also capable of restoring the math leading to that
of the Latin text (usually 1.2 times the font size). Finally,
it is possible to achieve the Microsoft Word multiple line
spacing style using zhlineskip.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/latex/zhlineskip
%doc %{_texmfdistdir}/doc/latex/zhlineskip

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
