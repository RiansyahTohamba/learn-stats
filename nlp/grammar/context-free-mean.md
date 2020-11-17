Context-free berarti semua aturan produksinya memiliki satu non-terminal di sisi kiri mereka. 

# mencari ("()", "()()", "(())()", ...)

Misalnya, tata bahasa yang mengenali string tanda kurung yang cocok ("()", "() ()", "(()) ()", ...) ini bebas konteks:

Context-free means all of its production rules have a single non-terminal on their left hand side. For example, this grammar which recognizes strings of matched parentheses ("()", "()()", "(())()", ...) is context-free:

S → SS
S → (S)
S → ()


# mencari {a^n b^n c^n : n >= 1} 

Now consider this other grammar which 'recognizes strings' of the form {a^n b^n c^n : n >= 1} (e.g. "abc", "aabbcc", "aaabbbccc"):

S  → abc
S  → aSBc
cB → WB
WB → WX
WX → BX
BX → Bc
bB → bb


Sisi kiri setiap aturan terdiri dari satu non-terminal (dalam hal ini selalu S, tetapi bisa jadi lebih banyak.)
The left-hand side of every rule consists of a single non-terminal (in this case it's always S, but there could be more.)

Jika non-terminal B diawali dengan terminal / karakter literal c, Anda menulis ulang istilah tersebut menjadi WB tetapi jika didahului oleh b, Anda memperluas ke bb sebagai gantinya. Mungkin inilah yang dimaksud dengan sensitivitas konteks dari tata bahasa yang peka konteks.

If the non-terminal B is preceded by the terminal/literal character c, you rewrite that term to WB but if it's preceded by b, you expand to bb instead. This is presumably what the context-sensitivity of context-sensitive grammars is alluding to.

# PDA = push down automation

Bahasa bebas konteks dapat dikenali sebagai push-down automata. Sedangkan mesin keadaan terbatas tidak menggunakan penyimpanan tambahan, yaitu keputusannya hanya didasarkan pada keadaan dan masukan saat ini, robot penekan juga memiliki tumpukan yang dapat digunakannya dan dapat mengintip di bagian atas tumpukan untuk mengambil keputusan.

A context-free language can be recognized a push-down automaton. Whereas a finite state machine makes use of no auxiliary storage, i.e. its decision is based only on its current state and input, a push-down automaton also has a stack at its disposal and can peek at the top of the stack for taking decisions.

Untuk melihatnya beraksi, Anda dapat mengurai tanda kurung bersarang dengan bergerak dari kiri ke kanan dan mendorong tanda kurung kiri ke tumpukan setiap kali Anda menemukannya, dan muncul setiap kali Anda menemukan tanda kurung kanan. Jika Anda tidak pernah mencoba untuk keluar dari tumpukan kosong, dan tumpukan kosong di akhir string, string tersebut valid.

To see that in action, you can parse nested parentheses by moving left to right and pushing a left parentheses onto a stack each time you encounter one, and popping each time you encounter a right parentheses. If you never end up trying to pop from an empty stack, and the stack's empty at the end of the string, the string is valid.

Untuk bahasa yang peka konteks, PDA tidak cukup. Anda akan membutuhkan robot berbatas linier yang seperti Mesin Turing yang pita perekatnya tidak terbatas (meskipun jumlah pita yang tersedia sebanding dengan masukan). Perhatikan bahwa itu menjelaskan komputer dengan cukup baik - kami suka menganggapnya sebagai Mesin Turing tetapi di dunia nyata Anda tidak dapat mengambil lebih banyak RAM mid-program secara sewenang-wenang. Jika tidak jelas bagi Anda bagaimana LBA lebih kuat daripada PDA, LBA dapat meniru PDA dengan menggunakan bagian pita sebagai tumpukan, tetapi LBA juga dapat memilih untuk menggunakan pita dengan cara lain.


For a context-sensitive language, a PDA isn't enough. You'll need a linear-bounded automaton which is like a Turing Machine whose tape isn't unlimited (though the amount of tape available is proportional to the input). Note that that describes computers pretty well - we like to think of them as Turing Machines but in the real world you can't grab arbitrarily more RAM mid-program. If it's not obvious to you how an LBA is more powerful than a PDA, an LBA can emulate a PDA by using part of its tape as a stack, but it can also choose to use its tape in other ways.

(Jika Anda bertanya-tanya apa yang dapat dikenali oleh Mesin Status Hingga, jawabannya adalah ekspresi reguler. Tetapi bukan ekspresi reguler pada steroid dengan grup penangkap dan lihat ke belakang / lihat ke depan yang Anda lihat dalam bahasa program; maksud saya yang dapat Anda buat dengan operator seperti [abc], |, *, +, dan?. Anda dapat melihat bahwa abbbz cocok dengan regex ab * z hanya dengan mempertahankan posisi Anda saat ini di string dan regex, tidak perlu stack.)

(If you're wondering what a Finite State Machine can recognize, the answer is regular expressions. But not the regexes on steroids with capture groups and look-behind/look-ahead you see in program languages; I mean the ones you can build with operators like [abc], |, *, +, and ?. You can see that abbbz matches regex ab*z just by keeping your current position in the string and regex, no stack required.)

# jawaban ke 2

The other answers are quite long, even if accurate and correct. This is the short version.
Jawaban lainnya cukup panjang, meskipun akurat dan benar. Ini adalah versi singkatnya.
Jika Anda memiliki serangkaian karakter (terminal dan nonterminals) dan Anda ingin mengganti nonterminal dalam string tersebut, tata bahasa bebas konteks memungkinkan Anda melakukannya terlepas dari karakter yang mengelilingi nonterminal.
If you have a string of characters (terminals and nonterminals) and you wish to replace a nonterminal in the string, a context-free grammar allows you to do that regardless of the characters surrounding the nonterminal.


Consider the following rules (lowercase are terminals, uppercase are nonterminals):

A -> a
AB -> a

Di aturan pertama, Anda bisa mengganti A terlepas dari apa yang muncul di sekitarnya (konteks). Dalam aturan kedua, Anda tidak dapat mengganti A kecuali diikuti oleh B. Meskipun kedua nonterminal akan diganti dalam kasus tersebut, poin pentingnya adalah bahwa nonterminal yang mengelilingi materi A. Seseorang tidak dapat mengganti BA dengan a, atau B dengan a: hanya A diikuti oleh B karena urutannya, konteks nonterminalnya penting. Artinya, konteks suatu masalah nonterminal pada aturan kedua, membuatnya peka konteks, sedangkan aturan pertama bebas konteks.
In the first rule, you can replace an A regardless of what appears around it (context). In the second rule, you cannot replace A unless it is followed by B. While both nonterminals will be replaced in that case, the important point is that the nonterminals surrounding the A matter. One cannot replace BA with a, or B with a: only an A followed by a B because the order, the context of the nonterminals is important. This means the context of a nonterminal matters in the second rule, making it context-sensitive, while the first rule is context-free.

# jawaban 3
The answers above give a pretty good definition of what it is. Let's see if I can put it in my own words, so that you will have 23 explanations instead of 20. The whole purpose of a grammar, any grammar, is to figure out if a particular sentence is a sentence in the given language. 

However, what we really use grammars and parsing for is to figure out what the sentence means. It's like the old diagramming of a sentence you may or may not have done back in English class back in school. A sentence is made of a subject part and a predicate part, a subject part has a noun and maybe some adjectives, a predicate part has a verb and perhaps an object noun, with some more adjectives, etc.

If there were a grammar for English (and I don't think there is, not in the computer science sense) then it would have rules of the following form, called productions.

Sentence -> SubjectPart PredicatePart
SubjectPart -> Adjective Noun
etc...

Anda kemudian dapat menulis sebuah program dan memberikannya kalimat apa saja, dan program tersebut dapat menggunakan tata bahasa untuk mencari tahu bagian mana dari kalimat tersebut setiap kata, dan apa hubungannya satu sama lain.
You could then write a program and hand it any sentence, and the program could use the grammar to figure out which part of the sentence each word is, and what relation they have to each other.
Jika dalam setiap produksi hanya ada satu hal di sisi kiri, maka itu berarti setiap kali Anda melihat sisi kanan dalam kalimat, Anda diperbolehkan menggantinya di sisi kiri. Misalnya, setiap kali Anda melihat kata benda kata sifat, Anda dapat mengatakan "Itu adalah Subjek" tanpa memperhatikan apa pun di luar frasa itu.


If in every production, there is only one thing on the left side, then that means that whenever you see the right side in the sentence, you are allowed to substitute in the left side. For instance whenever you saw adjective noun, you could say "That's a SubjectPart" without paying any attention to anything outside of that phrase.

Namun, bahasa Inggris (bahkan deskripsi bahasa Inggris yang saya berikan di atas) bersifat peka konteks. "Kata sifat kata sifat" tidak selalu merupakan SubjectPart, bisa jadi NounPhrase dalam PredicatePart. Itu tergantung konteksnya. Mari kembangkan sedikit tata bahasa pseudo-Inggris kita:

However, English (even the simplified description of English I gave above) is context-sensitive. "Adjective noun" isn't always a SubjectPart, it could be a NounPhrase in a PredicatePart. It depends on the context. Let's expand our pseudo-English grammar a bit:

Sentence -> SubjectPart PredicatePart
SubjectPart -> Adjective Noun
PredicatePart -> VerbPhrase ObjectNounPhrase
VerbPhrase ObjectNounPhrase -> VerbPhrase Adjective Noun


You can only make an "adjective noun" into an ObjectNounPhrase if it comes right after a VerbPhrase. Basically, if you have a production and you can apply it any time you want, no matter what surrounds it, it is context-free. You can always tell if a grammar is context free easily. Just check if there is more than one symbol on the left side of the arrows. Any language might be described by more than one grammar. If some grammar for a language is context-free, the language is context free. It can be proven for some languages that there is no context-free grammar possible. I suppose there might be a context-free grammar for the simplified pseudo-English subset I am describing above.
Anda hanya dapat membuat "kata sifat kata sifat" menjadi ObjectNounPhrase jika muncul tepat setelah VerbPhrase. Pada dasarnya, jika Anda memiliki produksi dan dapat menerapkannya kapan pun Anda mau, apa pun yang mengelilinginya, ini bebas konteks. Anda selalu dapat mengetahui apakah tata bahasa bebas konteks dengan mudah. Periksa saja apakah ada lebih dari satu simbol di sisi kiri panah. Bahasa apa pun dapat dijelaskan oleh lebih dari satu tata bahasa. Jika beberapa tata bahasa untuk suatu bahasa bebas konteks, maka bahasa tersebut bebas konteks. Beberapa bahasa dapat dibuktikan bahwa tidak ada tata bahasa bebas konteks yang memungkinkan. Saya kira mungkin ada tata bahasa bebas konteks untuk subset pseudo-Inggris sederhana yang saya jelaskan di atas.

As for why it matters, it requires a simpler kind of program to parse a context-free grammar. As noted in the other answers, it doesn't require the full power of a Turing machine to parse a context-free grammar. A lookahead LR(1) parser (which is a kind of pushdown machine) for a particular context-free grammar can parse any sentence in that grammar in time and space linear to the length of the sentence. If the sentence is in the language, the parser will produce a structure tree identifying what each symbol in the sentence means (or at least what part it plays in the structure). If the sentence is not in the grammar, the parser will notice and stop on the first symbol which is impossible to reconcile with the grammar and preceding symbols (on the first "error").
Adapun mengapa itu penting, itu membutuhkan jenis program yang lebih sederhana untuk mengurai tata bahasa bebas konteks. Seperti dicatat dalam jawaban lain, tidak memerlukan kekuatan penuh mesin Turing untuk mengurai tata bahasa bebas konteks. Pengurai lookahead LR (1) (yang merupakan sejenis mesin bentang bawah) untuk tata bahasa bebas konteks tertentu dapat mengurai kalimat apa pun dalam tata bahasa tersebut dalam ruang dan waktu yang linier dengan panjang kalimat. Jika kalimat tersebut dalam bahasa, parser akan menghasilkan pohon struktur yang mengidentifikasi arti setiap simbol dalam kalimat (atau setidaknya bagian apa yang dimainkannya dalam struktur). Jika kalimat tersebut tidak ada dalam tata bahasa, parser akan melihat dan berhenti pada simbol pertama yang tidak mungkin direkonsiliasi dengan tata bahasa dan simbol sebelumnya (pada "kesalahan" pertama).


What's even better is that there are programs which you can give a description of a grammar, and a list of instructions about what to do with each part (in a sense attaching a "meaning" to each production) and the program will write the parser for you. The program will parse the sentence, find the structure, and run your instructions on each part of the structure. This kind of program is called a parser-generator or compiler-compiler. This kind of language analysis was invented for automatic analysis of natural language (such as English) but it turns out that this is most useful for analyzing computer languages. A language designer can write a grammar which captures his new language, then run it through the parser-generator to get a program which parses his language, and translates, interprets, compiles, executes, etc if he wants.
Apa yang lebih baik adalah bahwa ada program yang dapat Anda berikan deskripsi tata bahasa, dan daftar instruksi tentang apa yang harus dilakukan dengan setiap bagian (dalam arti melampirkan "arti" untuk setiap produksi) dan program akan menulis parser untukmu. Program akan mengurai kalimat, menemukan strukturnya, dan menjalankan instruksi Anda pada setiap bagian struktur. Program semacam ini disebut parser-generator atau compiler-compiler. Jenis analisis bahasa ini ditemukan untuk analisis otomatis bahasa alami (seperti bahasa Inggris), tetapi ternyata ini paling berguna untuk menganalisis bahasa komputer. Seorang desainer bahasa dapat menulis tata bahasa yang menangkap bahasa barunya, kemudian menjalankannya melalui parser-generator untuk mendapatkan program yang mem-parsing bahasanya, dan menerjemahkan, menafsirkan, mengompilasi, mengeksekusi, dll jika dia mau.

Faktanya, dalam banyak kasus Anda tidak dapat melakukan ini. Misalnya, tanda kurung seimbang adalah bahasa tanpa konteks, tetapi bahasa yang diperlukan untuk mendeklarasikan semua variabel sebelum Anda menggunakannya adalah peka konteks. Pengurai adalah bagian dari kompilator, tetapi logika tambahan diperlukan untuk menerapkan persyaratan lain ini. Apa yang kemudian harus Anda lakukan adalah menulis tata bahasa yang menangkap sebanyak mungkin bahasa Anda, menjalankannya melalui generator parser, lalu menulis kode yang memberlakukan persyaratan lainnya (penangan tabel simbol, dll). Kami biasanya tidak menggunakan tata bahasa yang peka konteks karena dukungannya jauh lebih buruk. Saya tidak tahu apakah ada yang setara dengan generator parser LR (k) untuk bahasa sensitif konteks. Ya, mesin Turing (atau mesin terikat linier) dapat menguraikannya, tetapi saya tidak tahu apakah ada algoritme umum untuk mengubah tata bahasa sensitif konteks menjadi program untuk mesin Turing, dalam arti LR (1 ) generator membuat tabel parse untuk mesin pushdown. Dugaan saya adalah bahwa tabel yang mendasari parser akan menjadi lebih besar secara eksponensial. Bagaimanapun, siswa CS (seperti saya, dulu) biasanya diajarkan tata bahasa bebas konteks dan generator parser LR (1) seperti YACC.
In fact, in most cases you can't really do this. For instance, balanced parentheses are a context-free language, but a language where it is required to declare all variables before you use them is context-sensitive. The parser is a part of the compiler, but additional logic is required to enforce these other requirements. What you then have to do is write a grammar which captures as much of your language as possible, run that through a parser-generator, then write code which enforces the rest of the requirements (symbol table handler, etc). We don't generally use context-sensitive grammars because they are much more poorly supported. I don't know if there is an equivalent to an LR(k) parser-generator for context-sensitive languages. Yes, a Turing machine (or linear bound machine) can parse one, but I don't know if there is a general algorithm for turning a context-sensitive grammar into a program for a Turing machine, in the sense that an LR(1) generator makes parse tables for a pushdown machine. My guess is that the tables which underlie the parser would be exponentially larger. In any case, CS students (like myself, back in the day) are usually taught context-free grammars and LR(1) parser generators such as YACC.

tambahan
Production Rule
https://en.wikipedia.org/wiki/Production_%28computer_science%29
