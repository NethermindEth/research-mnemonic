/*
 @licstart  The following is the entire license notice for the JavaScript code in this file.

 The MIT License (MIT)

 Copyright (C) 1997-2020 by Dimitri van Heesch

 Permission is hereby granted, free of charge, to any person obtaining a copy of this software
 and associated documentation files (the "Software"), to deal in the Software without restriction,
 including without limitation the rights to use, copy, modify, merge, publish, distribute,
 sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is
 furnished to do so, subject to the following conditions:

 The above copyright notice and this permission notice shall be included in all copies or
 substantial portions of the Software.

 THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING
 BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
 NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM,
 DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

 @licend  The above is the entire license notice for the JavaScript code in this file
*/
var NAVTREE =
[
  [ "Mnemonic sharing", "index.html", [
    [ "Reference implementation for Mnemonics Research Project", "md_research_mnemonic__r_e_a_d_m_e.html", [
      [ "Table of contents", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md1", null ],
      [ "Description", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md2", null ],
      [ "Notation", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md3", null ],
      [ "Shamir secret sharing scheme", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md4", [
        [ "1. Share Generation Phase:", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md5", null ],
        [ "2. Reconstruction Phase:", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md6", null ]
      ] ],
      [ "Generating shares and reconstruction of the secret", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md7", [
        [ "Polynomial interpolation", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md8", null ],
        [ "Share Generation", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md9", [
          [ "INPUT: secret <em>s</em>, total number of shares <em>n</em>, threshold <em>t</em>, order of Galois field <em>q</em>, irreducible polynomial of GF(<em>q</em>)", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md10", null ],
          [ "OUTPUT: list of <em>n</em> shares", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md11", null ]
        ] ],
        [ "Secret Reconstruction", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md12", [
          [ "INPUT: list of share id <em>x</em>, list of access shares <em>y</em>, order of Galois field <em>q</em>, irreducible polynomial of GF(<em>q</em>), digest length <em>d</em>.", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md13", null ],
          [ "OUTPUT: secret <em>s'</em> or abort.", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md14", null ]
        ] ]
      ] ],
      [ "Basic usage", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md15", null ],
      [ "Format of a share", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md16", null ],
      [ "Design rationale", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md17", [
        [ "Role of the digest", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md18", null ],
        [ "Number of words and Galois field", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md19", null ],
        [ "Security", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md20", null ],
        [ "References", "md_research_mnemonic__r_e_a_d_m_e.html#autotoc_md21", null ]
      ] ]
    ] ],
    [ "Packages", "namespaces.html", [
      [ "Packages", "namespaces.html", "namespaces_dup" ],
      [ "Package Functions", "namespacemembers.html", [
        [ "All", "namespacemembers.html", null ],
        [ "Functions", "namespacemembers_func.html", null ]
      ] ]
    ] ]
  ] ]
];

var NAVTREEINDEX =
[
"index.html"
];

var SYNCONMSG = 'click to disable panel synchronisation';
var SYNCOFFMSG = 'click to enable panel synchronisation';