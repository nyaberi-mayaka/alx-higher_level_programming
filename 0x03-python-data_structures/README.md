<h1 align="center">0x03. Python - Data Structures: Lists, Tuples
</h1>

***
## Resources
**Read or watch:**
* [3.1.3. Lists](https://docs.python.org/3/tutorial/introduction.html#lists)
* [Data structures](https://docs.python.org/3/tutorial/datastructures.html) *(until `5.3. Tuples and Sequences` included)*
* [Learn to Program 6 : Lists](https://www.youtube.com/watch?v=A1HUzrvS-Pw)
* [Lists Telusko](https://www.youtube.com/watch?v=Eaz5e6M8tL4)
* [immutable](https://docs.python.org/3/glossary.html#term-immutable)
* [Lists documentation](https://docs.python.org/3/tutorial/introduction.html#lists)
***
## Learning Objectives
### General
* Why Python programming is awesome
* What are lists and how to use them
* What are the differences and similarities between strings and lists
* What are the most common methods of lists and how to use them
* How to use lists as stacks and queues
* What are list comprehensions and how to use them
* What are tuples and how to use them
* When to use tuples versus lists
* What is a sequence
* What is tuple packing
* What is sequence unpacking
* What is the `del` statement and how to use it

***
## Notes

<section id="sequence-types-list-tuple-range">
<span id="typesseq"></span><h2>Sequence Types — <a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code></a>, <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code></a>, <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal notranslate"><span class="pre">range</span></code></a><a class="headerlink" href="#sequence-types-list-tuple-range" title="Permalink to this headline">¶</a></h2>
<p>There are three basic sequence types: lists, tuples, and range objects.
Additional sequence types tailored for processing of
<a class="reference internal" href="#binaryseq"><span class="std std-ref">binary data</span></a> and <a class="reference internal" href="#textseq"><span class="std std-ref">text strings</span></a> are
described in dedicated sections.</p>
<section id="common-sequence-operations">
<span id="typesseq-common"></span><h3>Common Sequence Operations<a class="headerlink" href="#common-sequence-operations" title="Permalink to this headline">¶</a></h3>
<p id="index-18">The operations in the following table are supported by most sequence types,
both mutable and immutable. The <a class="reference internal" href="collections.abc.html#collections.abc.Sequence" title="collections.abc.Sequence"><code class="xref py py-class docutils literal notranslate"><span class="pre">collections.abc.Sequence</span></code></a> ABC is
provided to make it easier to correctly implement these operations on
custom sequence types.</p>
<p>This table lists the sequence operations sorted in ascending priority.  In the
table, <em>s</em> and <em>t</em> are sequences of the same type, <em>n</em>, <em>i</em>, <em>j</em> and <em>k</em> are
integers and <em>x</em> is an arbitrary object that meets any type and value
restrictions imposed by <em>s</em>.</p>
<p>The <code class="docutils literal notranslate"><span class="pre">in</span></code> and <code class="docutils literal notranslate"><span class="pre">not</span> <span class="pre">in</span></code> operations have the same priorities as the
comparison operations. The <code class="docutils literal notranslate"><span class="pre">+</span></code> (concatenation) and <code class="docutils literal notranslate"><span class="pre">*</span></code> (repetition)
operations have the same priority as the corresponding numeric operations. <a class="footnote-reference brackets" href="#id14" id="id4">3</a></p>
<div class="responsive-table__container"><table class="docutils align-default" id="index-19">
<colgroup>
<col style="width: 38%">
<col style="width: 47%">
<col style="width: 15%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Operation</p></th>
<th class="head"><p>Result</p></th>
<th class="head"><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">x</span> <span class="pre">in</span> <span class="pre">s</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">True</span></code> if an item of <em>s</em> is
equal to <em>x</em>, else <code class="docutils literal notranslate"><span class="pre">False</span></code></p></td>
<td><p>(1)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">x</span> <span class="pre">not</span> <span class="pre">in</span> <span class="pre">s</span></code></p></td>
<td><p><code class="docutils literal notranslate"><span class="pre">False</span></code> if an item of <em>s</em> is
equal to <em>x</em>, else <code class="docutils literal notranslate"><span class="pre">True</span></code></p></td>
<td><p>(1)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">+</span> <span class="pre">t</span></code></p></td>
<td><p>the concatenation of <em>s</em> and
<em>t</em></p></td>
<td><p>(6)(7)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">*</span> <span class="pre">n</span></code> or
<code class="docutils literal notranslate"><span class="pre">n</span> <span class="pre">*</span> <span class="pre">s</span></code></p></td>
<td><p>equivalent to adding <em>s</em> to
itself <em>n</em> times</p></td>
<td><p>(2)(7)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s[i]</span></code></p></td>
<td><p><em>i</em>th item of <em>s</em>, origin 0</p></td>
<td><p>(3)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s[i:j]</span></code></p></td>
<td><p>slice of <em>s</em> from <em>i</em> to <em>j</em></p></td>
<td><p>(3)(4)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s[i:j:k]</span></code></p></td>
<td><p>slice of <em>s</em> from <em>i</em> to <em>j</em>
with step <em>k</em></p></td>
<td><p>(3)(5)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">len(s)</span></code></p></td>
<td><p>length of <em>s</em></p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">min(s)</span></code></p></td>
<td><p>smallest item of <em>s</em></p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">max(s)</span></code></p></td>
<td><p>largest item of <em>s</em></p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s.index(x[,</span> <span class="pre">i[,</span> <span class="pre">j]])</span></code></p></td>
<td><p>index of the first occurrence
of <em>x</em> in <em>s</em> (at or after
index <em>i</em> and before index <em>j</em>)</p></td>
<td><p>(8)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s.count(x)</span></code></p></td>
<td><p>total number of occurrences of
<em>x</em> in <em>s</em></p></td>
<td></td>
</tr>
</tbody>
</table></div>
<p>Sequences of the same type also support comparisons.  In particular, tuples
and lists are compared lexicographically by comparing corresponding elements.
This means that to compare equal, every element must compare equal and the
two sequences must be of the same type and have the same length.  (For full
details see <a class="reference internal" href="../reference/expressions.html#comparisons"><span class="std std-ref">Comparisons</span></a> in the language reference.)</p>
<p id="index-20">Forward and reversed iterators over mutable sequences access values using an
index.  That index will continue to march forward (or backward) even if the
underlying sequence is mutated.  The iterator terminates only when an
<a class="reference internal" href="exceptions.html#IndexError" title="IndexError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">IndexError</span></code></a> or a <a class="reference internal" href="exceptions.html#StopIteration" title="StopIteration"><code class="xref py py-exc docutils literal notranslate"><span class="pre">StopIteration</span></code></a> is encountered (or when the index
drops below zero).</p>
<p>Notes:</p>
<ol class="arabic">
<li><p>While the <code class="docutils literal notranslate"><span class="pre">in</span></code> and <code class="docutils literal notranslate"><span class="pre">not</span> <span class="pre">in</span></code> operations are used only for simple
containment testing in the general case, some specialised sequences
(such as <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code></a>, <a class="reference internal" href="#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> and <a class="reference internal" href="#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a>) also use
them for subsequence testing:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">"gg"</span> <span class="ow">in</span> <span class="s2">"eggs"</span>
<span class="go">True</span>
</pre></div>
</div>
</li>
<li><p>Values of <em>n</em> less than <code class="docutils literal notranslate"><span class="pre">0</span></code> are treated as <code class="docutils literal notranslate"><span class="pre">0</span></code> (which yields an empty
sequence of the same type as <em>s</em>).  Note that items in the sequence <em>s</em>
are not copied; they are referenced multiple times.  This often haunts
new Python programmers; consider:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span> <span class="o">=</span> <span class="p">[[]]</span> <span class="o">*</span> <span class="mi">3</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span>
<span class="go">[[], [], []]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span>
<span class="go">[[3], [3], [3]]</span>
</pre></div>
</div>
<p>What has happened is that <code class="docutils literal notranslate"><span class="pre">[[]]</span></code> is a one-element list containing an empty
list, so all three elements of <code class="docutils literal notranslate"><span class="pre">[[]]</span> <span class="pre">*</span> <span class="pre">3</span></code> are references to this single empty
list.  Modifying any of the elements of <code class="docutils literal notranslate"><span class="pre">lists</span></code> modifies this single list.
You can create a list of different lists this way:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span> <span class="o">=</span> <span class="p">[[]</span> <span class="k">for</span> <span class="n">i</span> <span class="ow">in</span> <span class="nb">range</span><span class="p">(</span><span class="mi">3</span><span class="p">)]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">0</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">3</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">1</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span><span class="p">[</span><span class="mi">2</span><span class="p">]</span><span class="o">.</span><span class="n">append</span><span class="p">(</span><span class="mi">7</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">lists</span>
<span class="go">[[3], [5], [7]]</span>
</pre></div>
</div>
<p>Further explanation is available in the FAQ entry
<a class="reference internal" href="../faq/programming.html#faq-multidimensional-list"><span class="std std-ref">How do I create a multidimensional list?</span></a>.</p>
</li>
<li><p>If <em>i</em> or <em>j</em> is negative, the index is relative to the end of sequence <em>s</em>:
<code class="docutils literal notranslate"><span class="pre">len(s)</span> <span class="pre">+</span> <span class="pre">i</span></code> or <code class="docutils literal notranslate"><span class="pre">len(s)</span> <span class="pre">+</span> <span class="pre">j</span></code> is substituted.  But note that <code class="docutils literal notranslate"><span class="pre">-0</span></code> is
still <code class="docutils literal notranslate"><span class="pre">0</span></code>.</p></li>
<li><p>The slice of <em>s</em> from <em>i</em> to <em>j</em> is defined as the sequence of items with index
<em>k</em> such that <code class="docutils literal notranslate"><span class="pre">i</span> <span class="pre">&lt;=</span> <span class="pre">k</span> <span class="pre">&lt;</span> <span class="pre">j</span></code>.  If <em>i</em> or <em>j</em> is greater than <code class="docutils literal notranslate"><span class="pre">len(s)</span></code>, use
<code class="docutils literal notranslate"><span class="pre">len(s)</span></code>.  If <em>i</em> is omitted or <code class="docutils literal notranslate"><span class="pre">None</span></code>, use <code class="docutils literal notranslate"><span class="pre">0</span></code>.  If <em>j</em> is omitted or
<code class="docutils literal notranslate"><span class="pre">None</span></code>, use <code class="docutils literal notranslate"><span class="pre">len(s)</span></code>.  If <em>i</em> is greater than or equal to <em>j</em>, the slice is
empty.</p></li>
<li><p>The slice of <em>s</em> from <em>i</em> to <em>j</em> with step <em>k</em> is defined as the sequence of
items with index  <code class="docutils literal notranslate"><span class="pre">x</span> <span class="pre">=</span> <span class="pre">i</span> <span class="pre">+</span> <span class="pre">n*k</span></code> such that <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">&lt;=</span> <span class="pre">n</span> <span class="pre">&lt;</span> <span class="pre">(j-i)/k</span></code>.  In other words,
the indices are <code class="docutils literal notranslate"><span class="pre">i</span></code>, <code class="docutils literal notranslate"><span class="pre">i+k</span></code>, <code class="docutils literal notranslate"><span class="pre">i+2*k</span></code>, <code class="docutils literal notranslate"><span class="pre">i+3*k</span></code> and so on, stopping when
<em>j</em> is reached (but never including <em>j</em>).  When <em>k</em> is positive,
<em>i</em> and <em>j</em> are reduced to <code class="docutils literal notranslate"><span class="pre">len(s)</span></code> if they are greater.
When <em>k</em> is negative, <em>i</em> and <em>j</em> are reduced to <code class="docutils literal notranslate"><span class="pre">len(s)</span> <span class="pre">-</span> <span class="pre">1</span></code> if
they are greater.  If <em>i</em> or <em>j</em> are omitted or <code class="docutils literal notranslate"><span class="pre">None</span></code>, they become
“end” values (which end depends on the sign of <em>k</em>).  Note, <em>k</em> cannot be zero.
If <em>k</em> is <code class="docutils literal notranslate"><span class="pre">None</span></code>, it is treated like <code class="docutils literal notranslate"><span class="pre">1</span></code>.</p></li>
<li><p>Concatenating immutable sequences always results in a new object.  This
means that building up a sequence by repeated concatenation will have a
quadratic runtime cost in the total sequence length.  To get a linear
runtime cost, you must switch to one of the alternatives below:</p>
<ul class="simple">
<li><p>if concatenating <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code></a> objects, you can build a list and use
<a class="reference internal" href="#str.join" title="str.join"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.join()</span></code></a> at the end or else write to an <a class="reference internal" href="io.html#io.StringIO" title="io.StringIO"><code class="xref py py-class docutils literal notranslate"><span class="pre">io.StringIO</span></code></a>
instance and retrieve its value when complete</p></li>
<li><p>if concatenating <a class="reference internal" href="#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> objects, you can similarly use
<a class="reference internal" href="#bytes.join" title="bytes.join"><code class="xref py py-meth docutils literal notranslate"><span class="pre">bytes.join()</span></code></a> or <a class="reference internal" href="io.html#io.BytesIO" title="io.BytesIO"><code class="xref py py-class docutils literal notranslate"><span class="pre">io.BytesIO</span></code></a>, or you can do in-place
concatenation with a <a class="reference internal" href="#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a> object.  <a class="reference internal" href="#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a>
objects are mutable and have an efficient overallocation mechanism</p></li>
<li><p>if concatenating <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code></a> objects, extend a <a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code></a> instead</p></li>
<li><p>for other types, investigate the relevant class documentation</p></li>
</ul>
</li>
<li><p>Some sequence types (such as <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal notranslate"><span class="pre">range</span></code></a>) only support item sequences
that follow specific patterns, and hence don’t support sequence
concatenation or repetition.</p></li>
<li><p><code class="docutils literal notranslate"><span class="pre">index</span></code> raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">ValueError</span></code></a> when <em>x</em> is not found in <em>s</em>.
Not all implementations support passing the additional arguments <em>i</em> and <em>j</em>.
These arguments allow efficient searching of subsections of the sequence. Passing
the extra arguments is roughly equivalent to using <code class="docutils literal notranslate"><span class="pre">s[i:j].index(x)</span></code>, only
without copying any data and with the returned index being relative to
the start of the sequence rather than the start of the slice.</p></li>
</ol>
</section>
<section id="immutable-sequence-types">
<span id="typesseq-immutable"></span><h3>Immutable Sequence Types<a class="headerlink" href="#immutable-sequence-types" title="Permalink to this headline">¶</a></h3>
<p id="index-21">The only operation that immutable sequence types generally implement that is
not also implemented by mutable sequence types is support for the <a class="reference internal" href="functions.html#hash" title="hash"><code class="xref py py-func docutils literal notranslate"><span class="pre">hash()</span></code></a>
built-in.</p>
<p>This support allows immutable sequences, such as <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code></a> instances, to
be used as <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code></a> keys and stored in <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal notranslate"><span class="pre">set</span></code></a> and <a class="reference internal" href="#frozenset" title="frozenset"><code class="xref py py-class docutils literal notranslate"><span class="pre">frozenset</span></code></a>
instances.</p>
<p>Attempting to hash an immutable sequence that contains unhashable values will
result in <a class="reference internal" href="exceptions.html#TypeError" title="TypeError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">TypeError</span></code></a>.</p>
</section>
<section id="mutable-sequence-types">
<span id="typesseq-mutable"></span><h3>Mutable Sequence Types<a class="headerlink" href="#mutable-sequence-types" title="Permalink to this headline">¶</a></h3>
<p id="index-22">The operations in the following table are defined on mutable sequence types.
The <a class="reference internal" href="collections.abc.html#collections.abc.MutableSequence" title="collections.abc.MutableSequence"><code class="xref py py-class docutils literal notranslate"><span class="pre">collections.abc.MutableSequence</span></code></a> ABC is provided to make it
easier to correctly implement these operations on custom sequence types.</p>
<p>In the table <em>s</em> is an instance of a mutable sequence type, <em>t</em> is any
iterable object and <em>x</em> is an arbitrary object that meets any type
and value restrictions imposed by <em>s</em> (for example, <a class="reference internal" href="#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a> only
accepts integers that meet the value restriction <code class="docutils literal notranslate"><span class="pre">0</span> <span class="pre">&lt;=</span> <span class="pre">x</span> <span class="pre">&lt;=</span> <span class="pre">255</span></code>).</p>
<div class="responsive-table__container"><table class="docutils align-default" id="index-23">
<colgroup>
<col style="width: 36%">
<col style="width: 39%">
<col style="width: 25%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Operation</p></th>
<th class="head"><p>Result</p></th>
<th class="head"><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s[i]</span> <span class="pre">=</span> <span class="pre">x</span></code></p></td>
<td><p>item <em>i</em> of <em>s</em> is replaced by
<em>x</em></p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s[i:j]</span> <span class="pre">=</span> <span class="pre">t</span></code></p></td>
<td><p>slice of <em>s</em> from <em>i</em> to <em>j</em>
is replaced by the contents of
the iterable <em>t</em></p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">del</span> <span class="pre">s[i:j]</span></code></p></td>
<td><p>same as <code class="docutils literal notranslate"><span class="pre">s[i:j]</span> <span class="pre">=</span> <span class="pre">[]</span></code></p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s[i:j:k]</span> <span class="pre">=</span> <span class="pre">t</span></code></p></td>
<td><p>the elements of <code class="docutils literal notranslate"><span class="pre">s[i:j:k]</span></code>
are replaced by those of <em>t</em></p></td>
<td><p>(1)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">del</span> <span class="pre">s[i:j:k]</span></code></p></td>
<td><p>removes the elements of
<code class="docutils literal notranslate"><span class="pre">s[i:j:k]</span></code> from the list</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s.append(x)</span></code></p></td>
<td><p>appends <em>x</em> to the end of the
sequence (same as
<code class="docutils literal notranslate"><span class="pre">s[len(s):len(s)]</span> <span class="pre">=</span> <span class="pre">[x]</span></code>)</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s.clear()</span></code></p></td>
<td><p>removes all items from <em>s</em>
(same as <code class="docutils literal notranslate"><span class="pre">del</span> <span class="pre">s[:]</span></code>)</p></td>
<td><p>(5)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s.copy()</span></code></p></td>
<td><p>creates a shallow copy of <em>s</em>
(same as <code class="docutils literal notranslate"><span class="pre">s[:]</span></code>)</p></td>
<td><p>(5)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s.extend(t)</span></code> or
<code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">+=</span> <span class="pre">t</span></code></p></td>
<td><p>extends <em>s</em> with the
contents of <em>t</em> (for the
most part the same as
<code class="docutils literal notranslate"><span class="pre">s[len(s):len(s)]</span> <span class="pre">=</span> <span class="pre">t</span></code>)</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">*=</span> <span class="pre">n</span></code></p></td>
<td><p>updates <em>s</em> with its contents
repeated <em>n</em> times</p></td>
<td><p>(6)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s.insert(i,</span> <span class="pre">x)</span></code></p></td>
<td><p>inserts <em>x</em> into <em>s</em> at the
index given by <em>i</em>
(same as <code class="docutils literal notranslate"><span class="pre">s[i:i]</span> <span class="pre">=</span> <span class="pre">[x]</span></code>)</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s.pop()</span></code> or <code class="docutils literal notranslate"><span class="pre">s.pop(i)</span></code></p></td>
<td><p>retrieves the item at <em>i</em> and
also removes it from <em>s</em></p></td>
<td><p>(2)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">s.remove(x)</span></code></p></td>
<td><p>remove the first item from <em>s</em>
where <code class="docutils literal notranslate"><span class="pre">s[i]</span></code> is equal to <em>x</em></p></td>
<td><p>(3)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">s.reverse()</span></code></p></td>
<td><p>reverses the items of <em>s</em> in
place</p></td>
<td><p>(4)</p></td>
</tr>
</tbody>
</table></div>
<p>Notes:</p>
<ol class="arabic">
<li><p><em>t</em> must have the same length as the slice it is replacing.</p></li>
<li><p>The optional argument <em>i</em> defaults to <code class="docutils literal notranslate"><span class="pre">-1</span></code>, so that by default the last
item is removed and returned.</p></li>
<li><p><code class="xref py py-meth docutils literal notranslate"><span class="pre">remove()</span></code> raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">ValueError</span></code></a> when <em>x</em> is not found in <em>s</em>.</p></li>
<li><p>The <code class="xref py py-meth docutils literal notranslate"><span class="pre">reverse()</span></code> method modifies the sequence in place for economy of
space when reversing a large sequence.  To remind users that it operates by
side effect, it does not return the reversed sequence.</p></li>
<li><p><code class="xref py py-meth docutils literal notranslate"><span class="pre">clear()</span></code> and <code class="xref py py-meth docutils literal notranslate"><span class="pre">copy()</span></code> are included for consistency with the
interfaces of mutable containers that don’t support slicing operations
(such as <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code></a> and <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal notranslate"><span class="pre">set</span></code></a>). <code class="xref py py-meth docutils literal notranslate"><span class="pre">copy()</span></code> is not part of the
<a class="reference internal" href="collections.abc.html#collections.abc.MutableSequence" title="collections.abc.MutableSequence"><code class="xref py py-class docutils literal notranslate"><span class="pre">collections.abc.MutableSequence</span></code></a> ABC, but most concrete
mutable sequence classes provide it.</p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 3.3: </span><code class="xref py py-meth docutils literal notranslate"><span class="pre">clear()</span></code> and <code class="xref py py-meth docutils literal notranslate"><span class="pre">copy()</span></code> methods.</p>
</div>
</li>
<li><p>The value <em>n</em> is an integer, or an object implementing
<a class="reference internal" href="../reference/datamodel.html#object.__index__" title="object.__index__"><code class="xref py py-meth docutils literal notranslate"><span class="pre">__index__()</span></code></a>.  Zero and negative values of <em>n</em> clear
the sequence.  Items in the sequence are not copied; they are referenced
multiple times, as explained for <code class="docutils literal notranslate"><span class="pre">s</span> <span class="pre">*</span> <span class="pre">n</span></code> under <a class="reference internal" href="#typesseq-common"><span class="std std-ref">Common Sequence Operations</span></a>.</p></li>
</ol>
</section>
<section id="lists">
<span id="typesseq-list"></span><h3>Lists<a class="headerlink" href="#lists" title="Permalink to this headline">¶</a></h3>
<p id="index-24">Lists are mutable sequences, typically used to store collections of
homogeneous items (where the precise degree of similarity will vary by
application).</p>
<dl class="py class">
<dt class="sig sig-object py" id="list">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">list</span></span><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param"><span class="n"><span class="pre">iterable</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#list" title="Permalink to this definition">¶</a></dt>
<dd><p>Lists may be constructed in several ways:</p>
<ul class="simple">
<li><p>Using a pair of square brackets to denote the empty list: <code class="docutils literal notranslate"><span class="pre">[]</span></code></p></li>
<li><p>Using square brackets, separating items with commas: <code class="docutils literal notranslate"><span class="pre">[a]</span></code>, <code class="docutils literal notranslate"><span class="pre">[a,</span> <span class="pre">b,</span> <span class="pre">c]</span></code></p></li>
<li><p>Using a list comprehension: <code class="docutils literal notranslate"><span class="pre">[x</span> <span class="pre">for</span> <span class="pre">x</span> <span class="pre">in</span> <span class="pre">iterable]</span></code></p></li>
<li><p>Using the type constructor: <code class="docutils literal notranslate"><span class="pre">list()</span></code> or <code class="docutils literal notranslate"><span class="pre">list(iterable)</span></code></p></li>
</ul>
<p>The constructor builds a list whose items are the same and in the same
order as <em>iterable</em>’s items.  <em>iterable</em> may be either a sequence, a
container that supports iteration, or an iterator object.  If <em>iterable</em>
is already a list, a copy is made and returned, similar to <code class="docutils literal notranslate"><span class="pre">iterable[:]</span></code>.
For example, <code class="docutils literal notranslate"><span class="pre">list('abc')</span></code> returns <code class="docutils literal notranslate"><span class="pre">['a',</span> <span class="pre">'b',</span> <span class="pre">'c']</span></code> and
<code class="docutils literal notranslate"><span class="pre">list(</span> <span class="pre">(1,</span> <span class="pre">2,</span> <span class="pre">3)</span> <span class="pre">)</span></code> returns <code class="docutils literal notranslate"><span class="pre">[1,</span> <span class="pre">2,</span> <span class="pre">3]</span></code>.
If no argument is given, the constructor creates a new empty list, <code class="docutils literal notranslate"><span class="pre">[]</span></code>.</p>
<p>Many other operations also produce lists, including the <a class="reference internal" href="functions.html#sorted" title="sorted"><code class="xref py py-func docutils literal notranslate"><span class="pre">sorted()</span></code></a>
built-in.</p>
<p>Lists implement all of the <a class="reference internal" href="#typesseq-common"><span class="std std-ref">common</span></a> and
<a class="reference internal" href="#typesseq-mutable"><span class="std std-ref">mutable</span></a> sequence operations. Lists also provide the
following additional method:</p>
<dl class="py method">
<dt class="sig sig-object py" id="list.sort">
<span class="sig-name descname"><span class="pre">sort</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">*</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">key</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">reverse</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#list.sort" title="Permalink to this definition">¶</a></dt>
<dd><p>This method sorts the list in place, using only <code class="docutils literal notranslate"><span class="pre">&lt;</span></code> comparisons
between items. Exceptions are not suppressed - if any comparison operations
fail, the entire sort operation will fail (and the list will likely be left
in a partially modified state).</p>
<p><a class="reference internal" href="#list.sort" title="list.sort"><code class="xref py py-meth docutils literal notranslate"><span class="pre">sort()</span></code></a> accepts two arguments that can only be passed by keyword
(<a class="reference internal" href="../glossary.html#keyword-only-parameter"><span class="std std-ref">keyword-only arguments</span></a>):</p>
<p><em>key</em> specifies a function of one argument that is used to extract a
comparison key from each list element (for example, <code class="docutils literal notranslate"><span class="pre">key=str.lower</span></code>).
The key corresponding to each item in the list is calculated once and
then used for the entire sorting process. The default value of <code class="docutils literal notranslate"><span class="pre">None</span></code>
means that list items are sorted directly without calculating a separate
key value.</p>
<p>The <a class="reference internal" href="functools.html#functools.cmp_to_key" title="functools.cmp_to_key"><code class="xref py py-func docutils literal notranslate"><span class="pre">functools.cmp_to_key()</span></code></a> utility is available to convert a 2.x
style <em>cmp</em> function to a <em>key</em> function.</p>
<p><em>reverse</em> is a boolean value.  If set to <code class="docutils literal notranslate"><span class="pre">True</span></code>, then the list elements
are sorted as if each comparison were reversed.</p>
<p>This method modifies the sequence in place for economy of space when
sorting a large sequence.  To remind users that it operates by side
effect, it does not return the sorted sequence (use <a class="reference internal" href="functions.html#sorted" title="sorted"><code class="xref py py-func docutils literal notranslate"><span class="pre">sorted()</span></code></a> to
explicitly request a new sorted list instance).</p>
<p>The <a class="reference internal" href="#list.sort" title="list.sort"><code class="xref py py-meth docutils literal notranslate"><span class="pre">sort()</span></code></a> method is guaranteed to be stable.  A sort is stable if it
guarantees not to change the relative order of elements that compare equal
— this is helpful for sorting in multiple passes (for example, sort by
department, then by salary grade).</p>
<p>For sorting examples and a brief sorting tutorial, see <a class="reference internal" href="../howto/sorting.html#sortinghowto"><span class="std std-ref">Sorting HOW TO</span></a>.</p>
<div class="impl-detail compound">
<p><strong>CPython implementation detail:</strong> While a list is being sorted, the effect of attempting to mutate, or even
inspect, the list is undefined.  The C implementation of Python makes the
list appear empty for the duration, and raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">ValueError</span></code></a> if it can
detect that the list has been mutated during a sort.</p>
</div>
</dd></dl>

</dd></dl>

</section>
<section id="tuples">
<span id="typesseq-tuple"></span><h3>Tuples<a class="headerlink" href="#tuples" title="Permalink to this headline">¶</a></h3>
<p id="index-25">Tuples are immutable sequences, typically used to store collections of
heterogeneous data (such as the 2-tuples produced by the <a class="reference internal" href="functions.html#enumerate" title="enumerate"><code class="xref py py-func docutils literal notranslate"><span class="pre">enumerate()</span></code></a>
built-in). Tuples are also used for cases where an immutable sequence of
homogeneous data is needed (such as allowing storage in a <a class="reference internal" href="#set" title="set"><code class="xref py py-class docutils literal notranslate"><span class="pre">set</span></code></a> or
<a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code></a> instance).</p>
<dl class="py class">
<dt class="sig sig-object py" id="tuple">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">tuple</span></span><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param"><span class="n"><span class="pre">iterable</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#tuple" title="Permalink to this definition">¶</a></dt>
<dd><p>Tuples may be constructed in a number of ways:</p>
<ul class="simple">
<li><p>Using a pair of parentheses to denote the empty tuple: <code class="docutils literal notranslate"><span class="pre">()</span></code></p></li>
<li><p>Using a trailing comma for a singleton tuple: <code class="docutils literal notranslate"><span class="pre">a,</span></code> or <code class="docutils literal notranslate"><span class="pre">(a,)</span></code></p></li>
<li><p>Separating items with commas: <code class="docutils literal notranslate"><span class="pre">a,</span> <span class="pre">b,</span> <span class="pre">c</span></code> or <code class="docutils literal notranslate"><span class="pre">(a,</span> <span class="pre">b,</span> <span class="pre">c)</span></code></p></li>
<li><p>Using the <a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-func docutils literal notranslate"><span class="pre">tuple()</span></code></a> built-in: <code class="docutils literal notranslate"><span class="pre">tuple()</span></code> or <code class="docutils literal notranslate"><span class="pre">tuple(iterable)</span></code></p></li>
</ul>
<p>The constructor builds a tuple whose items are the same and in the same
order as <em>iterable</em>’s items.  <em>iterable</em> may be either a sequence, a
container that supports iteration, or an iterator object.  If <em>iterable</em>
is already a tuple, it is returned unchanged. For example,
<code class="docutils literal notranslate"><span class="pre">tuple('abc')</span></code> returns <code class="docutils literal notranslate"><span class="pre">('a',</span> <span class="pre">'b',</span> <span class="pre">'c')</span></code> and
<code class="docutils literal notranslate"><span class="pre">tuple(</span> <span class="pre">[1,</span> <span class="pre">2,</span> <span class="pre">3]</span> <span class="pre">)</span></code> returns <code class="docutils literal notranslate"><span class="pre">(1,</span> <span class="pre">2,</span> <span class="pre">3)</span></code>.
If no argument is given, the constructor creates a new empty tuple, <code class="docutils literal notranslate"><span class="pre">()</span></code>.</p>
<p>Note that it is actually the comma which makes a tuple, not the parentheses.
The parentheses are optional, except in the empty tuple case, or
when they are needed to avoid syntactic ambiguity. For example,
<code class="docutils literal notranslate"><span class="pre">f(a,</span> <span class="pre">b,</span> <span class="pre">c)</span></code> is a function call with three arguments, while
<code class="docutils literal notranslate"><span class="pre">f((a,</span> <span class="pre">b,</span> <span class="pre">c))</span></code> is a function call with a 3-tuple as the sole argument.</p>
<p>Tuples implement all of the <a class="reference internal" href="#typesseq-common"><span class="std std-ref">common</span></a> sequence
operations.</p>
</dd></dl>

<p>For heterogeneous collections of data where access by name is clearer than
access by index, <a class="reference internal" href="collections.html#collections.namedtuple" title="collections.namedtuple"><code class="xref py py-func docutils literal notranslate"><span class="pre">collections.namedtuple()</span></code></a> may be a more appropriate
choice than a simple tuple object.</p>
</section>
<section id="ranges">
<span id="typesseq-range"></span><h3>Ranges<a class="headerlink" href="#ranges" title="Permalink to this headline">¶</a></h3>
<p id="index-26">The <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal notranslate"><span class="pre">range</span></code></a> type represents an immutable sequence of numbers and is
commonly used for looping a specific number of times in <a class="reference internal" href="../reference/compound_stmts.html#for"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">for</span></code></a>
loops.</p>
<dl class="py class">
<dt class="sig sig-object py" id="range">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">range</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">stop</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#range" title="Permalink to this definition">¶</a></dt>
<dt class="sig sig-object py">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">range</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">start</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">stop</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">step</span></span></em><span class="optional">]</span><span class="sig-paren">)</span></dt>
<dd><p>The arguments to the range constructor must be integers (either built-in
<a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a> or any object that implements the <a class="reference internal" href="../reference/datamodel.html#object.__index__" title="object.__index__"><code class="xref py py-meth docutils literal notranslate"><span class="pre">__index__()</span></code></a> special
method).  If the <em>step</em> argument is omitted, it defaults to <code class="docutils literal notranslate"><span class="pre">1</span></code>.
If the <em>start</em> argument is omitted, it defaults to <code class="docutils literal notranslate"><span class="pre">0</span></code>.
If <em>step</em> is zero, <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">ValueError</span></code></a> is raised.</p>
<p>For a positive <em>step</em>, the contents of a range <code class="docutils literal notranslate"><span class="pre">r</span></code> are determined by the
formula <code class="docutils literal notranslate"><span class="pre">r[i]</span> <span class="pre">=</span> <span class="pre">start</span> <span class="pre">+</span> <span class="pre">step*i</span></code> where <code class="docutils literal notranslate"><span class="pre">i</span> <span class="pre">&gt;=</span> <span class="pre">0</span></code> and
<code class="docutils literal notranslate"><span class="pre">r[i]</span> <span class="pre">&lt;</span> <span class="pre">stop</span></code>.</p>
<p>For a negative <em>step</em>, the contents of the range are still determined by
the formula <code class="docutils literal notranslate"><span class="pre">r[i]</span> <span class="pre">=</span> <span class="pre">start</span> <span class="pre">+</span> <span class="pre">step*i</span></code>, but the constraints are <code class="docutils literal notranslate"><span class="pre">i</span> <span class="pre">&gt;=</span> <span class="pre">0</span></code>
and <code class="docutils literal notranslate"><span class="pre">r[i]</span> <span class="pre">&gt;</span> <span class="pre">stop</span></code>.</p>
<p>A range object will be empty if <code class="docutils literal notranslate"><span class="pre">r[0]</span></code> does not meet the value
constraint. Ranges do support negative indices, but these are interpreted
as indexing from the end of the sequence determined by the positive
indices.</p>
<p>Ranges containing absolute values larger than <a class="reference internal" href="sys.html#sys.maxsize" title="sys.maxsize"><code class="xref py py-data docutils literal notranslate"><span class="pre">sys.maxsize</span></code></a> are
permitted but some features (such as <a class="reference internal" href="functions.html#len" title="len"><code class="xref py py-func docutils literal notranslate"><span class="pre">len()</span></code></a>) may raise
<a class="reference internal" href="exceptions.html#OverflowError" title="OverflowError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">OverflowError</span></code></a>.</p>
<p>Range examples:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">10</span><span class="p">))</span>
<span class="go">[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">11</span><span class="p">))</span>
<span class="go">[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">30</span><span class="p">,</span> <span class="mi">5</span><span class="p">))</span>
<span class="go">[0, 5, 10, 15, 20, 25]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">10</span><span class="p">,</span> <span class="mi">3</span><span class="p">))</span>
<span class="go">[0, 3, 6, 9]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="o">-</span><span class="mi">10</span><span class="p">,</span> <span class="o">-</span><span class="mi">1</span><span class="p">))</span>
<span class="go">[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">))</span>
<span class="go">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="nb">list</span><span class="p">(</span><span class="nb">range</span><span class="p">(</span><span class="mi">1</span><span class="p">,</span> <span class="mi">0</span><span class="p">))</span>
<span class="go">[]</span>
</pre></div>
</div>
<p>Ranges implement all of the <a class="reference internal" href="#typesseq-common"><span class="std std-ref">common</span></a> sequence operations
except concatenation and repetition (due to the fact that range objects can
only represent sequences that follow a strict pattern and repetition and
concatenation will usually violate that pattern).</p>
<dl class="py attribute">
<dt class="sig sig-object py" id="range.start">
<span class="sig-name descname"><span class="pre">start</span></span><a class="headerlink" href="#range.start" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <em>start</em> parameter (or <code class="docutils literal notranslate"><span class="pre">0</span></code> if the parameter was
not supplied)</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="range.stop">
<span class="sig-name descname"><span class="pre">stop</span></span><a class="headerlink" href="#range.stop" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <em>stop</em> parameter</p>
</dd></dl>

<dl class="py attribute">
<dt class="sig sig-object py" id="range.step">
<span class="sig-name descname"><span class="pre">step</span></span><a class="headerlink" href="#range.step" title="Permalink to this definition">¶</a></dt>
<dd><p>The value of the <em>step</em> parameter (or <code class="docutils literal notranslate"><span class="pre">1</span></code> if the parameter was
not supplied)</p>
</dd></dl>

</dd></dl>

<p>The advantage of the <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal notranslate"><span class="pre">range</span></code></a> type over a regular <a class="reference internal" href="#list" title="list"><code class="xref py py-class docutils literal notranslate"><span class="pre">list</span></code></a> or
<a class="reference internal" href="#tuple" title="tuple"><code class="xref py py-class docutils literal notranslate"><span class="pre">tuple</span></code></a> is that a <a class="reference internal" href="#range" title="range"><code class="xref py py-class docutils literal notranslate"><span class="pre">range</span></code></a> object will always take the same
(small) amount of memory, no matter the size of the range it represents (as it
only stores the <code class="docutils literal notranslate"><span class="pre">start</span></code>, <code class="docutils literal notranslate"><span class="pre">stop</span></code> and <code class="docutils literal notranslate"><span class="pre">step</span></code> values, calculating individual
items and subranges as needed).</p>
<p>Range objects implement the <a class="reference internal" href="collections.abc.html#collections.abc.Sequence" title="collections.abc.Sequence"><code class="xref py py-class docutils literal notranslate"><span class="pre">collections.abc.Sequence</span></code></a> ABC, and provide
features such as containment tests, element index lookup, slicing and
support for negative indices (see <a class="reference internal" href="#typesseq"><span class="std std-ref">Sequence Types — list, tuple, range</span></a>):</p>
<div class="doctest highlight-default notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">r</span> <span class="o">=</span> <span class="nb">range</span><span class="p">(</span><span class="mi">0</span><span class="p">,</span> <span class="mi">20</span><span class="p">,</span> <span class="mi">2</span><span class="p">)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span>
<span class="go">range(0, 20, 2)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">11</span> <span class="ow">in</span> <span class="n">r</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="mi">10</span> <span class="ow">in</span> <span class="n">r</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="o">.</span><span class="n">index</span><span class="p">(</span><span class="mi">10</span><span class="p">)</span>
<span class="go">5</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="p">[</span><span class="mi">5</span><span class="p">]</span>
<span class="go">10</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="p">[:</span><span class="mi">5</span><span class="p">]</span>
<span class="go">range(0, 10, 2)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">r</span><span class="p">[</span><span class="o">-</span><span class="mi">1</span><span class="p">]</span>
<span class="go">18</span>
</pre></div>
</div>
<p>Testing range objects for equality with <code class="docutils literal notranslate"><span class="pre">==</span></code> and <code class="docutils literal notranslate"><span class="pre">!=</span></code> compares
them as sequences.  That is, two range objects are considered equal if
they represent the same sequence of values.  (Note that two range
objects that compare equal might have different <a class="reference internal" href="#range.start" title="range.start"><code class="xref py py-attr docutils literal notranslate"><span class="pre">start</span></code></a>,
<a class="reference internal" href="#range.stop" title="range.stop"><code class="xref py py-attr docutils literal notranslate"><span class="pre">stop</span></code></a> and <a class="reference internal" href="#range.step" title="range.step"><code class="xref py py-attr docutils literal notranslate"><span class="pre">step</span></code></a> attributes, for example
<code class="docutils literal notranslate"><span class="pre">range(0)</span> <span class="pre">==</span> <span class="pre">range(2,</span> <span class="pre">1,</span> <span class="pre">3)</span></code> or <code class="docutils literal notranslate"><span class="pre">range(0,</span> <span class="pre">3,</span> <span class="pre">2)</span> <span class="pre">==</span> <span class="pre">range(0,</span> <span class="pre">4,</span> <span class="pre">2)</span></code>.)</p>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.2: </span>Implement the Sequence ABC.
Support slicing and negative indices.
Test <a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a> objects for membership in constant time instead of
iterating through all items.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.3: </span>Define ‘==’ and ‘!=’ to compare range objects based on the
sequence of values they define (instead of comparing based on
object identity).</p>
</div>
<div class="versionadded">
<p><span class="versionmodified added">New in version 3.3: </span>The <a class="reference internal" href="#range.start" title="range.start"><code class="xref py py-attr docutils literal notranslate"><span class="pre">start</span></code></a>, <a class="reference internal" href="#range.stop" title="range.stop"><code class="xref py py-attr docutils literal notranslate"><span class="pre">stop</span></code></a> and <a class="reference internal" href="#range.step" title="range.step"><code class="xref py py-attr docutils literal notranslate"><span class="pre">step</span></code></a>
attributes.</p>
</div>
<div class="admonition seealso">
<p class="admonition-title">See also</p>
<ul class="simple">
<li><p>The <a class="reference external" href="https://code.activestate.com/recipes/579000/">linspace recipe</a>
shows how to implement a lazy version of range suitable for floating
point applications.</p></li>
</ul>
</div>
</section>
</section>
<section id="text-sequence-type-str">
<span id="textseq"></span><span id="index-27"></span><h2>Text Sequence Type — <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code></a><a class="headerlink" href="#text-sequence-type-str" title="Permalink to this headline">¶</a></h2>
<p>Textual data in Python is handled with <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code></a> objects, or <em class="dfn">strings</em>.
Strings are immutable
<a class="reference internal" href="#typesseq"><span class="std std-ref">sequences</span></a> of Unicode code points.  String literals are
written in a variety of ways:</p>
<ul class="simple">
<li><p>Single quotes: <code class="docutils literal notranslate"><span class="pre">'allows</span> <span class="pre">embedded</span> <span class="pre">"double"</span> <span class="pre">quotes'</span></code></p></li>
<li><p>Double quotes: <code class="docutils literal notranslate"><span class="pre">"allows</span> <span class="pre">embedded</span> <span class="pre">'single'</span> <span class="pre">quotes"</span></code></p></li>
<li><p>Triple quoted: <code class="docutils literal notranslate"><span class="pre">'''Three</span> <span class="pre">single</span> <span class="pre">quotes'''</span></code>, <code class="docutils literal notranslate"><span class="pre">"""Three</span> <span class="pre">double</span> <span class="pre">quotes"""</span></code></p></li>
</ul>
<p>Triple quoted strings may span multiple lines - all associated whitespace will
be included in the string literal.</p>
<p>String literals that are part of a single expression and have only whitespace
between them will be implicitly converted to a single string literal. That
is, <code class="docutils literal notranslate"><span class="pre">("spam</span> <span class="pre">"</span> <span class="pre">"eggs")</span> <span class="pre">==</span> <span class="pre">"spam</span> <span class="pre">eggs"</span></code>.</p>
<p>See <a class="reference internal" href="../reference/lexical_analysis.html#strings"><span class="std std-ref">String and Bytes literals</span></a> for more about the various forms of string literal,
including supported escape sequences, and the <code class="docutils literal notranslate"><span class="pre">r</span></code> (“raw”) prefix that
disables most escape sequence processing.</p>
<p>Strings may also be created from other objects using the <a class="reference internal" href="#str" title="str"><code class="xref py py-class docutils literal notranslate"><span class="pre">str</span></code></a>
constructor.</p>
<p>Since there is no separate “character” type, indexing a string produces
strings of length 1. That is, for a non-empty string <em>s</em>, <code class="docutils literal notranslate"><span class="pre">s[0]</span> <span class="pre">==</span> <span class="pre">s[0:1]</span></code>.</p>
<p id="index-28">There is also no mutable string type, but <a class="reference internal" href="#str.join" title="str.join"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.join()</span></code></a> or
<a class="reference internal" href="io.html#io.StringIO" title="io.StringIO"><code class="xref py py-class docutils literal notranslate"><span class="pre">io.StringIO</span></code></a> can be used to efficiently construct strings from
multiple fragments.</p>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.3: </span>For backwards compatibility with the Python 2 series, the <code class="docutils literal notranslate"><span class="pre">u</span></code> prefix is
once again permitted on string literals. It has no effect on the meaning
of string literals and cannot be combined with the <code class="docutils literal notranslate"><span class="pre">r</span></code> prefix.</p>
</div>
<span class="target" id="index-29"></span><dl class="py class">
<dt class="sig sig-object py" id="str">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">str</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">object</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">''</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str" title="Permalink to this definition">¶</a></dt>
<dt class="sig sig-object py">
<em class="property"><span class="pre">class</span><span class="w"> </span></em><span class="sig-name descname"><span class="pre">str</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">object</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">b''</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">encoding</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'utf-8'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">errors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'strict'</span></span></em><span class="sig-paren">)</span></dt>
<dd><p>Return a <a class="reference internal" href="#textseq"><span class="std std-ref">string</span></a> version of <em>object</em>.  If <em>object</em> is not
provided, returns the empty string.  Otherwise, the behavior of <code class="docutils literal notranslate"><span class="pre">str()</span></code>
depends on whether <em>encoding</em> or <em>errors</em> is given, as follows.</p>
<p>If neither <em>encoding</em> nor <em>errors</em> is given, <code class="docutils literal notranslate"><span class="pre">str(object)</span></code> returns
<a class="reference internal" href="../reference/datamodel.html#object.__str__" title="object.__str__"><code class="xref py py-meth docutils literal notranslate"><span class="pre">type(object).__str__(object)</span></code></a>,
which is the “informal” or nicely
printable string representation of <em>object</em>.  For string objects, this is
the string itself.  If <em>object</em> does not have a <a class="reference internal" href="../reference/datamodel.html#object.__str__" title="object.__str__"><code class="xref py py-meth docutils literal notranslate"><span class="pre">__str__()</span></code></a>
method, then <a class="reference internal" href="#str" title="str"><code class="xref py py-func docutils literal notranslate"><span class="pre">str()</span></code></a> falls back to returning
<a class="reference internal" href="functions.html#repr" title="repr"><code class="xref py py-meth docutils literal notranslate"><span class="pre">repr(object)</span></code></a>.</p>
<p id="index-30">If at least one of <em>encoding</em> or <em>errors</em> is given, <em>object</em> should be a
<a class="reference internal" href="../glossary.html#term-bytes-like-object"><span class="xref std std-term">bytes-like object</span></a> (e.g. <a class="reference internal" href="#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> or <a class="reference internal" href="#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a>).  In
this case, if <em>object</em> is a <a class="reference internal" href="#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> (or <a class="reference internal" href="#bytearray" title="bytearray"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytearray</span></code></a>) object,
then <code class="docutils literal notranslate"><span class="pre">str(bytes,</span> <span class="pre">encoding,</span> <span class="pre">errors)</span></code> is equivalent to
<a class="reference internal" href="#bytes.decode" title="bytes.decode"><code class="xref py py-meth docutils literal notranslate"><span class="pre">bytes.decode(encoding,</span> <span class="pre">errors)</span></code></a>.  Otherwise, the bytes
object underlying the buffer object is obtained before calling
<a class="reference internal" href="#bytes.decode" title="bytes.decode"><code class="xref py py-meth docutils literal notranslate"><span class="pre">bytes.decode()</span></code></a>.  See <a class="reference internal" href="#binaryseq"><span class="std std-ref">Binary Sequence Types — bytes, bytearray, memoryview</span></a> and
<a class="reference internal" href="../c-api/buffer.html#bufferobjects"><span class="std std-ref">Buffer Protocol</span></a> for information on buffer objects.</p>
<p>Passing a <a class="reference internal" href="#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> object to <a class="reference internal" href="#str" title="str"><code class="xref py py-func docutils literal notranslate"><span class="pre">str()</span></code></a> without the <em>encoding</em>
or <em>errors</em> arguments falls under the first case of returning the informal
string representation (see also the <a class="reference internal" href="../using/cmdline.html#cmdoption-b"><code class="xref std std-option docutils literal notranslate"><span class="pre">-b</span></code></a> command-line option to
Python).  For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">str</span><span class="p">(</span><span class="sa">b</span><span class="s1">'Zoot!'</span><span class="p">)</span>
<span class="go">"b'Zoot!'"</span>
</pre></div>
</div>
<p>For more information on the <code class="docutils literal notranslate"><span class="pre">str</span></code> class and its methods, see
<a class="reference internal" href="#textseq"><span class="std std-ref">Text Sequence Type — str</span></a> and the <a class="reference internal" href="#string-methods"><span class="std std-ref">String Methods</span></a> section below.  To output
formatted strings, see the <a class="reference internal" href="../reference/lexical_analysis.html#f-strings"><span class="std std-ref">Formatted string literals</span></a> and <a class="reference internal" href="string.html#formatstrings"><span class="std std-ref">Format String Syntax</span></a>
sections.  In addition, see the <a class="reference internal" href="text.html#stringservices"><span class="std std-ref">Text Processing Services</span></a> section.</p>
</dd></dl>

<section id="string-methods">
<span id="index-31"></span><span id="id5"></span><h3>String Methods<a class="headerlink" href="#string-methods" title="Permalink to this headline">¶</a></h3>
<p id="index-32">Strings implement all of the <a class="reference internal" href="#typesseq-common"><span class="std std-ref">common</span></a> sequence
operations, along with the additional methods described below.</p>
<p>Strings also support two styles of string formatting, one providing a large
degree of flexibility and customization (see <a class="reference internal" href="#str.format" title="str.format"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.format()</span></code></a>,
<a class="reference internal" href="string.html#formatstrings"><span class="std std-ref">Format String Syntax</span></a> and <a class="reference internal" href="string.html#string-formatting"><span class="std std-ref">Custom String Formatting</span></a>) and the other based on C
<code class="docutils literal notranslate"><span class="pre">printf</span></code> style formatting that handles a narrower range of types and is
slightly harder to use correctly, but is often faster for the cases it can
handle (<a class="reference internal" href="#old-string-formatting"><span class="std std-ref">printf-style String Formatting</span></a>).</p>
<p>The <a class="reference internal" href="text.html#textservices"><span class="std std-ref">Text Processing Services</span></a> section of the standard library covers a number of
other modules that provide various text related utilities (including regular
expression support in the <a class="reference internal" href="re.html#module-re" title="re: Regular expression operations."><code class="xref py py-mod docutils literal notranslate"><span class="pre">re</span></code></a> module).</p>
<dl class="py method">
<dt class="sig sig-object py" id="str.capitalize">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">capitalize</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.capitalize" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with its first character capitalized and the
rest lowercased.</p>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.8: </span>The first character is now put into titlecase rather than uppercase.
This means that characters like digraphs will only have their first
letter capitalized, instead of the full character.</p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.casefold">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">casefold</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.casefold" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a casefolded copy of the string. Casefolded strings may be used for
caseless matching.</p>
<p>Casefolding is similar to lowercasing but more aggressive because it is
intended to remove all case distinctions in a string. For example, the German
lowercase letter <code class="docutils literal notranslate"><span class="pre">'ß'</span></code> is equivalent to <code class="docutils literal notranslate"><span class="pre">"ss"</span></code>. Since it is already
lowercase, <a class="reference internal" href="#str.lower" title="str.lower"><code class="xref py py-meth docutils literal notranslate"><span class="pre">lower()</span></code></a> would do nothing to <code class="docutils literal notranslate"><span class="pre">'ß'</span></code>; <a class="reference internal" href="#str.casefold" title="str.casefold"><code class="xref py py-meth docutils literal notranslate"><span class="pre">casefold()</span></code></a>
converts it to <code class="docutils literal notranslate"><span class="pre">"ss"</span></code>.</p>
<p>The casefolding algorithm is described in section 3.13 of the Unicode
Standard.</p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 3.3.</span></p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.center">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">center</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">width</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">fillchar</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.center" title="Permalink to this definition">¶</a></dt>
<dd><p>Return centered in a string of length <em>width</em>. Padding is done using the
specified <em>fillchar</em> (default is an ASCII space). The original string is
returned if <em>width</em> is less than or equal to <code class="docutils literal notranslate"><span class="pre">len(s)</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.count">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">count</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sub</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">start</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">end</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.count" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the number of non-overlapping occurrences of substring <em>sub</em> in the
range [<em>start</em>, <em>end</em>].  Optional arguments <em>start</em> and <em>end</em> are
interpreted as in slice notation.</p>
<p>If <em>sub</em> is empty, returns the number of empty strings between characters
which is the length of the string plus one.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.encode">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">encode</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">encoding</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'utf-8'</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">errors</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">'strict'</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.encode" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the string encoded to <a class="reference internal" href="#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a>.</p>
<p><em>encoding</em> defaults to <code class="docutils literal notranslate"><span class="pre">'utf-8'</span></code>;
see <a class="reference internal" href="codecs.html#standard-encodings"><span class="std std-ref">Standard Encodings</span></a> for possible values.</p>
<p><em>errors</em> controls how encoding errors are handled.
If <code class="docutils literal notranslate"><span class="pre">'strict'</span></code> (the default), a <a class="reference internal" href="exceptions.html#UnicodeError" title="UnicodeError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">UnicodeError</span></code></a> exception is raised.
Other possible values are <code class="docutils literal notranslate"><span class="pre">'ignore'</span></code>,
<code class="docutils literal notranslate"><span class="pre">'replace'</span></code>, <code class="docutils literal notranslate"><span class="pre">'xmlcharrefreplace'</span></code>, <code class="docutils literal notranslate"><span class="pre">'backslashreplace'</span></code> and any
other name registered via <a class="reference internal" href="codecs.html#codecs.register_error" title="codecs.register_error"><code class="xref py py-func docutils literal notranslate"><span class="pre">codecs.register_error()</span></code></a>.
See <a class="reference internal" href="codecs.html#error-handlers"><span class="std std-ref">Error Handlers</span></a> for details.</p>
<p>For performance reasons, the value of <em>errors</em> is not checked for validity
unless an encoding error actually occurs,
<a class="reference internal" href="devmode.html#devmode"><span class="std std-ref">Python Development Mode</span></a> is enabled
or a <a class="reference internal" href="../using/configure.html#debug-build"><span class="std std-ref">debug build</span></a> is used.</p>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.1: </span>Added support for keyword arguments.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.9: </span>The value of the <em>errors</em> argument is now checked in <a class="reference internal" href="devmode.html#devmode"><span class="std std-ref">Python Development Mode</span></a> and
in <a class="reference internal" href="../using/configure.html#debug-build"><span class="std std-ref">debug mode</span></a>.</p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.endswith">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">endswith</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">suffix</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">start</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">end</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.endswith" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if the string ends with the specified <em>suffix</em>, otherwise return
<code class="docutils literal notranslate"><span class="pre">False</span></code>.  <em>suffix</em> can also be a tuple of suffixes to look for.  With optional
<em>start</em>, test beginning at that position.  With optional <em>end</em>, stop comparing
at that position.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.expandtabs">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">expandtabs</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">tabsize</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">8</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.expandtabs" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string where all tab characters are replaced by one or
more spaces, depending on the current column and the given tab size.  Tab
positions occur every <em>tabsize</em> characters (default is 8, giving tab
positions at columns 0, 8, 16 and so on).  To expand the string, the current
column is set to zero and the string is examined character by character.  If
the character is a tab (<code class="docutils literal notranslate"><span class="pre">\t</span></code>), one or more space characters are inserted
in the result until the current column is equal to the next tab position.
(The tab character itself is not copied.)  If the character is a newline
(<code class="docutils literal notranslate"><span class="pre">\n</span></code>) or return (<code class="docutils literal notranslate"><span class="pre">\r</span></code>), it is copied and the current column is reset to
zero.  Any other character is copied unchanged and the current column is
incremented by one regardless of how the character is represented when
printed.</p>
<div class="doctest highlight-default notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'01</span><span class="se">\t</span><span class="s1">012</span><span class="se">\t</span><span class="s1">0123</span><span class="se">\t</span><span class="s1">01234'</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">()</span>
<span class="go">'01      012     0123    01234'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'01</span><span class="se">\t</span><span class="s1">012</span><span class="se">\t</span><span class="s1">0123</span><span class="se">\t</span><span class="s1">01234'</span><span class="o">.</span><span class="n">expandtabs</span><span class="p">(</span><span class="mi">4</span><span class="p">)</span>
<span class="go">'01  012 0123    01234'</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.find">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">find</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sub</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">start</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">end</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.find" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the lowest index in the string where substring <em>sub</em> is found within
the slice <code class="docutils literal notranslate"><span class="pre">s[start:end]</span></code>.  Optional arguments <em>start</em> and <em>end</em> are
interpreted as in slice notation.  Return <code class="docutils literal notranslate"><span class="pre">-1</span></code> if <em>sub</em> is not found.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>The <a class="reference internal" href="#str.find" title="str.find"><code class="xref py py-meth docutils literal notranslate"><span class="pre">find()</span></code></a> method should be used only if you need to know the
position of <em>sub</em>.  To check if <em>sub</em> is a substring or not, use the
<a class="reference internal" href="../reference/expressions.html#in"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">in</span></code></a> operator:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'Py'</span> <span class="ow">in</span> <span class="s1">'Python'</span>
<span class="go">True</span>
</pre></div>
</div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.format">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">format</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="o"><span class="pre">*</span></span><span class="n"><span class="pre">args</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">**</span></span><span class="n"><span class="pre">kwargs</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.format" title="Permalink to this definition">¶</a></dt>
<dd><p>Perform a string formatting operation.  The string on which this method is
called can contain literal text or replacement fields delimited by braces
<code class="docutils literal notranslate"><span class="pre">{}</span></code>.  Each replacement field contains either the numeric index of a
positional argument, or the name of a keyword argument.  Returns a copy of
the string where each replacement field is replaced with the string value of
the corresponding argument.</p>
<div class="doctest highlight-default notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">"The sum of 1 + 2 is </span><span class="si">{0}</span><span class="s2">"</span><span class="o">.</span><span class="n">format</span><span class="p">(</span><span class="mi">1</span><span class="o">+</span><span class="mi">2</span><span class="p">)</span>
<span class="go">'The sum of 1 + 2 is 3'</span>
</pre></div>
</div>
<p>See <a class="reference internal" href="string.html#formatstrings"><span class="std std-ref">Format String Syntax</span></a> for a description of the various formatting options
that can be specified in format strings.</p>
<div class="admonition note">
<p class="admonition-title">Note</p>
<p>When formatting a number (<a class="reference internal" href="functions.html#int" title="int"><code class="xref py py-class docutils literal notranslate"><span class="pre">int</span></code></a>, <a class="reference internal" href="functions.html#float" title="float"><code class="xref py py-class docutils literal notranslate"><span class="pre">float</span></code></a>, <a class="reference internal" href="functions.html#complex" title="complex"><code class="xref py py-class docutils literal notranslate"><span class="pre">complex</span></code></a>,
<a class="reference internal" href="decimal.html#decimal.Decimal" title="decimal.Decimal"><code class="xref py py-class docutils literal notranslate"><span class="pre">decimal.Decimal</span></code></a> and subclasses) with the <code class="docutils literal notranslate"><span class="pre">n</span></code> type
(ex: <code class="docutils literal notranslate"><span class="pre">'{:n}'.format(1234)</span></code>), the function temporarily sets the
<code class="docutils literal notranslate"><span class="pre">LC_CTYPE</span></code> locale to the <code class="docutils literal notranslate"><span class="pre">LC_NUMERIC</span></code> locale to decode
<code class="docutils literal notranslate"><span class="pre">decimal_point</span></code> and <code class="docutils literal notranslate"><span class="pre">thousands_sep</span></code> fields of <code class="xref c c-func docutils literal notranslate"><span class="pre">localeconv()</span></code> if
they are non-ASCII or longer than 1 byte, and the <code class="docutils literal notranslate"><span class="pre">LC_NUMERIC</span></code> locale is
different than the <code class="docutils literal notranslate"><span class="pre">LC_CTYPE</span></code> locale.  This temporary change affects
other threads.</p>
</div>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.7: </span>When formatting a number with the <code class="docutils literal notranslate"><span class="pre">n</span></code> type, the function sets
temporarily the <code class="docutils literal notranslate"><span class="pre">LC_CTYPE</span></code> locale to the <code class="docutils literal notranslate"><span class="pre">LC_NUMERIC</span></code> locale in some
cases.</p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.format_map">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">format_map</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">mapping</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.format_map" title="Permalink to this definition">¶</a></dt>
<dd><p>Similar to <code class="docutils literal notranslate"><span class="pre">str.format(**mapping)</span></code>, except that <code class="docutils literal notranslate"><span class="pre">mapping</span></code> is
used directly and not copied to a <a class="reference internal" href="#dict" title="dict"><code class="xref py py-class docutils literal notranslate"><span class="pre">dict</span></code></a>.  This is useful
if for example <code class="docutils literal notranslate"><span class="pre">mapping</span></code> is a dict subclass:</p>
<div class="doctest highlight-default notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="k">class</span> <span class="nc">Default</span><span class="p">(</span><span class="nb">dict</span><span class="p">):</span>
<span class="gp">... </span>    <span class="k">def</span> <span class="fm">__missing__</span><span class="p">(</span><span class="bp">self</span><span class="p">,</span> <span class="n">key</span><span class="p">):</span>
<span class="gp">... </span>        <span class="k">return</span> <span class="n">key</span>
<span class="gp">...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'</span><span class="si">{name}</span><span class="s1"> was born in </span><span class="si">{country}</span><span class="s1">'</span><span class="o">.</span><span class="n">format_map</span><span class="p">(</span><span class="n">Default</span><span class="p">(</span><span class="n">name</span><span class="o">=</span><span class="s1">'Guido'</span><span class="p">))</span>
<span class="go">'Guido was born in country'</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified added">New in version 3.2.</span></p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.index">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">index</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sub</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">start</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">end</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.index" title="Permalink to this definition">¶</a></dt>
<dd><p>Like <a class="reference internal" href="#str.find" title="str.find"><code class="xref py py-meth docutils literal notranslate"><span class="pre">find()</span></code></a>, but raise <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">ValueError</span></code></a> when the substring is
not found.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isalnum">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isalnum</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isalnum" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all characters in the string are alphanumeric and there is at
least one character, <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.  A character <code class="docutils literal notranslate"><span class="pre">c</span></code> is alphanumeric if one
of the following returns <code class="docutils literal notranslate"><span class="pre">True</span></code>: <code class="docutils literal notranslate"><span class="pre">c.isalpha()</span></code>, <code class="docutils literal notranslate"><span class="pre">c.isdecimal()</span></code>,
<code class="docutils literal notranslate"><span class="pre">c.isdigit()</span></code>, or <code class="docutils literal notranslate"><span class="pre">c.isnumeric()</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isalpha">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isalpha</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isalpha" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all characters in the string are alphabetic and there is at least
one character, <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.  Alphabetic characters are those characters defined
in the Unicode character database as “Letter”, i.e., those with general category
property being one of “Lm”, “Lt”, “Lu”, “Ll”, or “Lo”.  Note that this is different
from the “Alphabetic” property defined in the Unicode Standard.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isascii">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isascii</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isascii" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if the string is empty or all characters in the string are ASCII,
<code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.
ASCII characters have code points in the range U+0000-U+007F.</p>
<div class="versionadded">
<p><span class="versionmodified added">New in version 3.7.</span></p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isdecimal">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isdecimal</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isdecimal" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all characters in the string are decimal
characters and there is at least one character, <code class="docutils literal notranslate"><span class="pre">False</span></code>
otherwise. Decimal characters are those that can be used to form
numbers in base 10, e.g. U+0660, ARABIC-INDIC DIGIT
ZERO.  Formally a decimal character is a character in the Unicode
General Category “Nd”.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isdigit">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isdigit</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isdigit" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all characters in the string are digits and there is at least one
character, <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.  Digits include decimal characters and digits that need
special handling, such as the compatibility superscript digits.
This covers digits which cannot be used to form numbers in base 10,
like the Kharosthi numbers.  Formally, a digit is a character that has the
property value Numeric_Type=Digit or Numeric_Type=Decimal.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isidentifier">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isidentifier</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isidentifier" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if the string is a valid identifier according to the language
definition, section <a class="reference internal" href="../reference/lexical_analysis.html#identifiers"><span class="std std-ref">Identifiers and keywords</span></a>.</p>
<p>Call <a class="reference internal" href="keyword.html#keyword.iskeyword" title="keyword.iskeyword"><code class="xref py py-func docutils literal notranslate"><span class="pre">keyword.iskeyword()</span></code></a> to test whether string <code class="docutils literal notranslate"><span class="pre">s</span></code> is a reserved
identifier, such as <a class="reference internal" href="../reference/compound_stmts.html#def"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">def</span></code></a> and <a class="reference internal" href="../reference/compound_stmts.html#class"><code class="xref std std-keyword docutils literal notranslate"><span class="pre">class</span></code></a>.</p>
<p>Example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">from</span> <span class="nn">keyword</span> <span class="kn">import</span> <span class="n">iskeyword</span>

<span class="gp">&gt;&gt;&gt; </span><span class="s1">'hello'</span><span class="o">.</span><span class="n">isidentifier</span><span class="p">(),</span> <span class="n">iskeyword</span><span class="p">(</span><span class="s1">'hello'</span><span class="p">)</span>
<span class="go">(True, False)</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'def'</span><span class="o">.</span><span class="n">isidentifier</span><span class="p">(),</span> <span class="n">iskeyword</span><span class="p">(</span><span class="s1">'def'</span><span class="p">)</span>
<span class="go">(True, True)</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.islower">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">islower</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.islower" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all cased characters <a class="footnote-reference brackets" href="#id15" id="id6">4</a> in the string are lowercase and
there is at least one cased character, <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isnumeric">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isnumeric</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isnumeric" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all characters in the string are numeric
characters, and there is at least one character, <code class="docutils literal notranslate"><span class="pre">False</span></code>
otherwise. Numeric characters include digit characters, and all characters
that have the Unicode numeric value property, e.g. U+2155,
VULGAR FRACTION ONE FIFTH.  Formally, numeric characters are those with the property
value Numeric_Type=Digit, Numeric_Type=Decimal or Numeric_Type=Numeric.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isprintable">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isprintable</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isprintable" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all characters in the string are printable or the string is
empty, <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.  Nonprintable characters are those characters defined
in the Unicode character database as “Other” or “Separator”, excepting the
ASCII space (0x20) which is considered printable.  (Note that printable
characters in this context are those which should not be escaped when
<a class="reference internal" href="functions.html#repr" title="repr"><code class="xref py py-func docutils literal notranslate"><span class="pre">repr()</span></code></a> is invoked on a string.  It has no bearing on the handling of
strings written to <a class="reference internal" href="sys.html#sys.stdout" title="sys.stdout"><code class="xref py py-data docutils literal notranslate"><span class="pre">sys.stdout</span></code></a> or <a class="reference internal" href="sys.html#sys.stderr" title="sys.stderr"><code class="xref py py-data docutils literal notranslate"><span class="pre">sys.stderr</span></code></a>.)</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isspace">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isspace</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isspace" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if there are only whitespace characters in the string and there is
at least one character, <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.</p>
<p>A character is <em>whitespace</em> if in the Unicode character database
(see <a class="reference internal" href="unicodedata.html#module-unicodedata" title="unicodedata: Access the Unicode Database."><code class="xref py py-mod docutils literal notranslate"><span class="pre">unicodedata</span></code></a>), either its general category is <code class="docutils literal notranslate"><span class="pre">Zs</span></code>
(“Separator, space”), or its bidirectional class is one of <code class="docutils literal notranslate"><span class="pre">WS</span></code>,
<code class="docutils literal notranslate"><span class="pre">B</span></code>, or <code class="docutils literal notranslate"><span class="pre">S</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.istitle">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">istitle</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.istitle" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if the string is a titlecased string and there is at least one
character, for example uppercase characters may only follow uncased characters
and lowercase characters only cased ones.  Return <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.isupper">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">isupper</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.isupper" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if all cased characters <a class="footnote-reference brackets" href="#id15" id="id7">4</a> in the string are uppercase and
there is at least one cased character, <code class="docutils literal notranslate"><span class="pre">False</span></code> otherwise.</p>
<div class="doctest highlight-default notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'BANANA'</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span>
<span class="go">True</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'banana'</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'baNana'</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span>
<span class="go">False</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">' '</span><span class="o">.</span><span class="n">isupper</span><span class="p">()</span>
<span class="go">False</span>
</pre></div>
</div>
</dd></dl>

<span class="target" id="meth-str-join"></span><dl class="py method">
<dt class="sig sig-object py" id="str.join">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">join</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">iterable</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.join" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a string which is the concatenation of the strings in <em>iterable</em>.
A <a class="reference internal" href="exceptions.html#TypeError" title="TypeError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">TypeError</span></code></a> will be raised if there are any non-string values in
<em>iterable</em>, including <a class="reference internal" href="#bytes" title="bytes"><code class="xref py py-class docutils literal notranslate"><span class="pre">bytes</span></code></a> objects.  The separator between
elements is the string providing this method.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.ljust">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">ljust</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">width</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">fillchar</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.ljust" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the string left justified in a string of length <em>width</em>. Padding is
done using the specified <em>fillchar</em> (default is an ASCII space). The
original string is returned if <em>width</em> is less than or equal to <code class="docutils literal notranslate"><span class="pre">len(s)</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.lower">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">lower</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.lower" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with all the cased characters <a class="footnote-reference brackets" href="#id15" id="id8">4</a> converted to
lowercase.</p>
<p>The lowercasing algorithm used is described in section 3.13 of the Unicode
Standard.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.lstrip">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">lstrip</span></span><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param"><span class="n"><span class="pre">chars</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.lstrip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with leading characters removed.  The <em>chars</em>
argument is a string specifying the set of characters to be removed.  If omitted
or <code class="docutils literal notranslate"><span class="pre">None</span></code>, the <em>chars</em> argument defaults to removing whitespace.  The <em>chars</em>
argument is not a prefix; rather, all combinations of its values are stripped:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'   spacious   '</span><span class="o">.</span><span class="n">lstrip</span><span class="p">()</span>
<span class="go">'spacious   '</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'www.example.com'</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s1">'cmowz.'</span><span class="p">)</span>
<span class="go">'example.com'</span>
</pre></div>
</div>
<p>See <a class="reference internal" href="#str.removeprefix" title="str.removeprefix"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.removeprefix()</span></code></a> for a method that will remove a single prefix
string rather than all of a set of characters.  For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'Arthur: three!'</span><span class="o">.</span><span class="n">lstrip</span><span class="p">(</span><span class="s1">'Arthur: '</span><span class="p">)</span>
<span class="go">'ee!'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'Arthur: three!'</span><span class="o">.</span><span class="n">removeprefix</span><span class="p">(</span><span class="s1">'Arthur: '</span><span class="p">)</span>
<span class="go">'three!'</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.maketrans">
<em class="property"><span class="pre">static</span><span class="w"> </span></em><span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">maketrans</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">x</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">y</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">z</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.maketrans" title="Permalink to this definition">¶</a></dt>
<dd><p>This static method returns a translation table usable for <a class="reference internal" href="#str.translate" title="str.translate"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.translate()</span></code></a>.</p>
<p>If there is only one argument, it must be a dictionary mapping Unicode
ordinals (integers) or characters (strings of length 1) to Unicode ordinals,
strings (of arbitrary lengths) or <code class="docutils literal notranslate"><span class="pre">None</span></code>.  Character keys will then be
converted to ordinals.</p>
<p>If there are two arguments, they must be strings of equal length, and in the
resulting dictionary, each character in x will be mapped to the character at
the same position in y.  If there is a third argument, it must be a string,
whose characters will be mapped to <code class="docutils literal notranslate"><span class="pre">None</span></code> in the result.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.partition">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">partition</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sep</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.partition" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the string at the first occurrence of <em>sep</em>, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
the string itself, followed by two empty strings.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.removeprefix">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">removeprefix</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">prefix</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">/</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.removeprefix" title="Permalink to this definition">¶</a></dt>
<dd><p>If the string starts with the <em>prefix</em> string, return
<code class="docutils literal notranslate"><span class="pre">string[len(prefix):]</span></code>. Otherwise, return a copy of the original
string:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'TestHook'</span><span class="o">.</span><span class="n">removeprefix</span><span class="p">(</span><span class="s1">'Test'</span><span class="p">)</span>
<span class="go">'Hook'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'BaseTestCase'</span><span class="o">.</span><span class="n">removeprefix</span><span class="p">(</span><span class="s1">'Test'</span><span class="p">)</span>
<span class="go">'BaseTestCase'</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified added">New in version 3.9.</span></p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.removesuffix">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">removesuffix</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">suffix</span></span></em>, <em class="sig-param"><span class="o"><span class="pre">/</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.removesuffix" title="Permalink to this definition">¶</a></dt>
<dd><p>If the string ends with the <em>suffix</em> string and that <em>suffix</em> is not empty,
return <code class="docutils literal notranslate"><span class="pre">string[:-len(suffix)]</span></code>. Otherwise, return a copy of the
original string:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'MiscTests'</span><span class="o">.</span><span class="n">removesuffix</span><span class="p">(</span><span class="s1">'Tests'</span><span class="p">)</span>
<span class="go">'Misc'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'TmpDirMixin'</span><span class="o">.</span><span class="n">removesuffix</span><span class="p">(</span><span class="s1">'Tests'</span><span class="p">)</span>
<span class="go">'TmpDirMixin'</span>
</pre></div>
</div>
<div class="versionadded">
<p><span class="versionmodified added">New in version 3.9.</span></p>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.replace">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">replace</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">old</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">new</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">count</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.replace" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with all occurrences of substring <em>old</em> replaced by
<em>new</em>.  If the optional argument <em>count</em> is given, only the first <em>count</em>
occurrences are replaced.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.rfind">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">rfind</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sub</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">start</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">end</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rfind" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the highest index in the string where substring <em>sub</em> is found, such
that <em>sub</em> is contained within <code class="docutils literal notranslate"><span class="pre">s[start:end]</span></code>.  Optional arguments <em>start</em>
and <em>end</em> are interpreted as in slice notation.  Return <code class="docutils literal notranslate"><span class="pre">-1</span></code> on failure.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.rindex">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">rindex</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sub</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">start</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">end</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rindex" title="Permalink to this definition">¶</a></dt>
<dd><p>Like <a class="reference internal" href="#str.rfind" title="str.rfind"><code class="xref py py-meth docutils literal notranslate"><span class="pre">rfind()</span></code></a> but raises <a class="reference internal" href="exceptions.html#ValueError" title="ValueError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">ValueError</span></code></a> when the substring <em>sub</em> is not
found.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.rjust">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">rjust</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">width</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">fillchar</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rjust" title="Permalink to this definition">¶</a></dt>
<dd><p>Return the string right justified in a string of length <em>width</em>. Padding is
done using the specified <em>fillchar</em> (default is an ASCII space). The
original string is returned if <em>width</em> is less than or equal to <code class="docutils literal notranslate"><span class="pre">len(s)</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.rpartition">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">rpartition</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sep</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.rpartition" title="Permalink to this definition">¶</a></dt>
<dd><p>Split the string at the last occurrence of <em>sep</em>, and return a 3-tuple
containing the part before the separator, the separator itself, and the part
after the separator.  If the separator is not found, return a 3-tuple containing
two empty strings, followed by the string itself.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.rsplit">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">rsplit</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sep</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">maxsplit</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-</span> <span class="pre">1</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.rsplit" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of the words in the string, using <em>sep</em> as the delimiter string.
If <em>maxsplit</em> is given, at most <em>maxsplit</em> splits are done, the <em>rightmost</em>
ones.  If <em>sep</em> is not specified or <code class="docutils literal notranslate"><span class="pre">None</span></code>, any whitespace string is a
separator.  Except for splitting from the right, <a class="reference internal" href="#str.rsplit" title="str.rsplit"><code class="xref py py-meth docutils literal notranslate"><span class="pre">rsplit()</span></code></a> behaves like
<a class="reference internal" href="#str.split" title="str.split"><code class="xref py py-meth docutils literal notranslate"><span class="pre">split()</span></code></a> which is described in detail below.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.rstrip">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">rstrip</span></span><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param"><span class="n"><span class="pre">chars</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.rstrip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with trailing characters removed.  The <em>chars</em>
argument is a string specifying the set of characters to be removed.  If omitted
or <code class="docutils literal notranslate"><span class="pre">None</span></code>, the <em>chars</em> argument defaults to removing whitespace.  The <em>chars</em>
argument is not a suffix; rather, all combinations of its values are stripped:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'   spacious   '</span><span class="o">.</span><span class="n">rstrip</span><span class="p">()</span>
<span class="go">'   spacious'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'mississippi'</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="s1">'ipz'</span><span class="p">)</span>
<span class="go">'mississ'</span>
</pre></div>
</div>
<p>See <a class="reference internal" href="#str.removesuffix" title="str.removesuffix"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.removesuffix()</span></code></a> for a method that will remove a single suffix
string rather than all of a set of characters.  For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'Monty Python'</span><span class="o">.</span><span class="n">rstrip</span><span class="p">(</span><span class="s1">' Python'</span><span class="p">)</span>
<span class="go">'M'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'Monty Python'</span><span class="o">.</span><span class="n">removesuffix</span><span class="p">(</span><span class="s1">' Python'</span><span class="p">)</span>
<span class="go">'Monty'</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.split">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">split</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">sep</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">None</span></span></em>, <em class="sig-param"><span class="n"><span class="pre">maxsplit</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">-</span> <span class="pre">1</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.split" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of the words in the string, using <em>sep</em> as the delimiter
string.  If <em>maxsplit</em> is given, at most <em>maxsplit</em> splits are done (thus,
the list will have at most <code class="docutils literal notranslate"><span class="pre">maxsplit+1</span></code> elements).  If <em>maxsplit</em> is not
specified or <code class="docutils literal notranslate"><span class="pre">-1</span></code>, then there is no limit on the number of splits
(all possible splits are made).</p>
<p>If <em>sep</em> is given, consecutive delimiters are not grouped together and are
deemed to delimit empty strings (for example, <code class="docutils literal notranslate"><span class="pre">'1,,2'.split(',')</span></code> returns
<code class="docutils literal notranslate"><span class="pre">['1',</span> <span class="pre">'',</span> <span class="pre">'2']</span></code>).  The <em>sep</em> argument may consist of multiple characters
(for example, <code class="docutils literal notranslate"><span class="pre">'1&lt;&gt;2&lt;&gt;3'.split('&lt;&gt;')</span></code> returns <code class="docutils literal notranslate"><span class="pre">['1',</span> <span class="pre">'2',</span> <span class="pre">'3']</span></code>).
Splitting an empty string with a specified separator returns <code class="docutils literal notranslate"><span class="pre">['']</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'1,2,3'</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">','</span><span class="p">)</span>
<span class="go">['1', '2', '3']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'1,2,3'</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">','</span><span class="p">,</span> <span class="n">maxsplit</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="go">['1', '2,3']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'1,2,,3,'</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">','</span><span class="p">)</span>
<span class="go">['1', '2', '', '3', '']</span>
</pre></div>
</div>
<p>If <em>sep</em> is not specified or is <code class="docutils literal notranslate"><span class="pre">None</span></code>, a different splitting algorithm is
applied: runs of consecutive whitespace are regarded as a single separator,
and the result will contain no empty strings at the start or end if the
string has leading or trailing whitespace.  Consequently, splitting an empty
string or a string consisting of just whitespace with a <code class="docutils literal notranslate"><span class="pre">None</span></code> separator
returns <code class="docutils literal notranslate"><span class="pre">[]</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'1 2 3'</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="go">['1', '2', '3']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'1 2 3'</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="n">maxsplit</span><span class="o">=</span><span class="mi">1</span><span class="p">)</span>
<span class="go">['1', '2 3']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'   1   2   3   '</span><span class="o">.</span><span class="n">split</span><span class="p">()</span>
<span class="go">['1', '2', '3']</span>
</pre></div>
</div>
</dd></dl>

<span class="target" id="index-33"></span><dl class="py method">
<dt class="sig sig-object py" id="str.splitlines">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">splitlines</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">keepends</span></span><span class="o"><span class="pre">=</span></span><span class="default_value"><span class="pre">False</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.splitlines" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a list of the lines in the string, breaking at line boundaries.  Line
breaks are not included in the resulting list unless <em>keepends</em> is given and
true.</p>
<p>This method splits on the following line boundaries.  In particular, the
boundaries are a superset of <a class="reference internal" href="../glossary.html#term-universal-newlines"><span class="xref std std-term">universal newlines</span></a>.</p>
<div class="responsive-table__container"><table class="docutils align-default">
<colgroup>
<col style="width: 44%">
<col style="width: 56%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Representation</p></th>
<th class="head"><p>Description</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">\n</span></code></p></td>
<td><p>Line Feed</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">\r</span></code></p></td>
<td><p>Carriage Return</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">\r\n</span></code></p></td>
<td><p>Carriage Return + Line Feed</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">\v</span></code> or <code class="docutils literal notranslate"><span class="pre">\x0b</span></code></p></td>
<td><p>Line Tabulation</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">\f</span></code> or <code class="docutils literal notranslate"><span class="pre">\x0c</span></code></p></td>
<td><p>Form Feed</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">\x1c</span></code></p></td>
<td><p>File Separator</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">\x1d</span></code></p></td>
<td><p>Group Separator</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">\x1e</span></code></p></td>
<td><p>Record Separator</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">\x85</span></code></p></td>
<td><p>Next Line (C1 Control Code)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">\u2028</span></code></p></td>
<td><p>Line Separator</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">\u2029</span></code></p></td>
<td><p>Paragraph Separator</p></td>
</tr>
</tbody>
</table></div>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.2: </span><code class="docutils literal notranslate"><span class="pre">\v</span></code> and <code class="docutils literal notranslate"><span class="pre">\f</span></code> added to list of line boundaries.</p>
</div>
<p>For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'ab c</span><span class="se">\n\n</span><span class="s1">de fg</span><span class="se">\r</span><span class="s1">kl</span><span class="se">\r\n</span><span class="s1">'</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">['ab c', '', 'de fg', 'kl']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'ab c</span><span class="se">\n\n</span><span class="s1">de fg</span><span class="se">\r</span><span class="s1">kl</span><span class="se">\r\n</span><span class="s1">'</span><span class="o">.</span><span class="n">splitlines</span><span class="p">(</span><span class="n">keepends</span><span class="o">=</span><span class="kc">True</span><span class="p">)</span>
<span class="go">['ab c\n', '\n', 'de fg\r', 'kl\r\n']</span>
</pre></div>
</div>
<p>Unlike <a class="reference internal" href="#str.split" title="str.split"><code class="xref py py-meth docutils literal notranslate"><span class="pre">split()</span></code></a> when a delimiter string <em>sep</em> is given, this
method returns an empty list for the empty string, and a terminal line
break does not result in an extra line:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">""</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">[]</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">"One line</span><span class="se">\n</span><span class="s2">"</span><span class="o">.</span><span class="n">splitlines</span><span class="p">()</span>
<span class="go">['One line']</span>
</pre></div>
</div>
<p>For comparison, <code class="docutils literal notranslate"><span class="pre">split('\n')</span></code> gives:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">''</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
<span class="go">['']</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'Two lines</span><span class="se">\n</span><span class="s1">'</span><span class="o">.</span><span class="n">split</span><span class="p">(</span><span class="s1">'</span><span class="se">\n</span><span class="s1">'</span><span class="p">)</span>
<span class="go">['Two lines', '']</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.startswith">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">startswith</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">prefix</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">start</span></span></em><span class="optional">[</span>, <em class="sig-param"><span class="n"><span class="pre">end</span></span></em><span class="optional">]</span><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.startswith" title="Permalink to this definition">¶</a></dt>
<dd><p>Return <code class="docutils literal notranslate"><span class="pre">True</span></code> if string starts with the <em>prefix</em>, otherwise return <code class="docutils literal notranslate"><span class="pre">False</span></code>.
<em>prefix</em> can also be a tuple of prefixes to look for.  With optional <em>start</em>,
test string beginning at that position.  With optional <em>end</em>, stop comparing
string at that position.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.strip">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">strip</span></span><span class="sig-paren">(</span><span class="optional">[</span><em class="sig-param"><span class="n"><span class="pre">chars</span></span></em><span class="optional">]</span><span class="sig-paren">)</span><a class="headerlink" href="#str.strip" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with the leading and trailing characters removed.
The <em>chars</em> argument is a string specifying the set of characters to be removed.
If omitted or <code class="docutils literal notranslate"><span class="pre">None</span></code>, the <em>chars</em> argument defaults to removing whitespace.
The <em>chars</em> argument is not a prefix or suffix; rather, all combinations of its
values are stripped:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'   spacious   '</span><span class="o">.</span><span class="n">strip</span><span class="p">()</span>
<span class="go">'spacious'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s1">'www.example.com'</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">'cmowz.'</span><span class="p">)</span>
<span class="go">'example'</span>
</pre></div>
</div>
<p>The outermost leading and trailing <em>chars</em> argument values are stripped
from the string. Characters are removed from the leading end until
reaching a string character that is not contained in the set of
characters in <em>chars</em>. A similar action takes place on the trailing end.
For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="n">comment_string</span> <span class="o">=</span> <span class="s1">'#....... Section 3.2.1 Issue #32 .......'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">comment_string</span><span class="o">.</span><span class="n">strip</span><span class="p">(</span><span class="s1">'.#! '</span><span class="p">)</span>
<span class="go">'Section 3.2.1 Issue #32'</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.swapcase">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">swapcase</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.swapcase" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with uppercase characters converted to lowercase and
vice versa. Note that it is not necessarily true that
<code class="docutils literal notranslate"><span class="pre">s.swapcase().swapcase()</span> <span class="pre">==</span> <span class="pre">s</span></code>.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.title">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">title</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.title" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a titlecased version of the string where words start with an uppercase
character and the remaining characters are lowercase.</p>
<p>For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s1">'Hello world'</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
<span class="go">'Hello World'</span>
</pre></div>
</div>
<p>The algorithm uses a simple language-independent definition of a word as
groups of consecutive letters.  The definition works in many contexts but
it means that apostrophes in contractions and possessives form word
boundaries, which may not be the desired result:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">"they're bill's friends from the UK"</span><span class="o">.</span><span class="n">title</span><span class="p">()</span>
<span class="go">"They'Re Bill'S Friends From The Uk"</span>
</pre></div>
</div>
<p>The <a class="reference internal" href="string.html#string.capwords" title="string.capwords"><code class="xref py py-func docutils literal notranslate"><span class="pre">string.capwords()</span></code></a> function does not have this problem, as it
splits words on spaces only.</p>
<p>Alternatively, a workaround for apostrophes can be constructed using regular
expressions:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="kn">import</span> <span class="nn">re</span>
<span class="gp">&gt;&gt;&gt; </span><span class="k">def</span> <span class="nf">titlecase</span><span class="p">(</span><span class="n">s</span><span class="p">):</span>
<span class="gp">... </span>    <span class="k">return</span> <span class="n">re</span><span class="o">.</span><span class="n">sub</span><span class="p">(</span><span class="sa">r</span><span class="s2">"[A-Za-z]+('[A-Za-z]+)?"</span><span class="p">,</span>
<span class="gp">... </span>                  <span class="k">lambda</span> <span class="n">mo</span><span class="p">:</span> <span class="n">mo</span><span class="o">.</span><span class="n">group</span><span class="p">(</span><span class="mi">0</span><span class="p">)</span><span class="o">.</span><span class="n">capitalize</span><span class="p">(),</span>
<span class="gp">... </span>                  <span class="n">s</span><span class="p">)</span>
<span class="gp">...</span>
<span class="gp">&gt;&gt;&gt; </span><span class="n">titlecase</span><span class="p">(</span><span class="s2">"they're bill's friends."</span><span class="p">)</span>
<span class="go">"They're Bill's Friends."</span>
</pre></div>
</div>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.translate">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">translate</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">table</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.translate" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string in which each character has been mapped through
the given translation table.  The table must be an object that implements
indexing via <code class="xref py py-meth docutils literal notranslate"><span class="pre">__getitem__()</span></code>, typically a <a class="reference internal" href="../glossary.html#term-mapping"><span class="xref std std-term">mapping</span></a> or
<a class="reference internal" href="../glossary.html#term-sequence"><span class="xref std std-term">sequence</span></a>.  When indexed by a Unicode ordinal (an integer), the
table object can do any of the following: return a Unicode ordinal or a
string, to map the character to one or more other characters; return
<code class="docutils literal notranslate"><span class="pre">None</span></code>, to delete the character from the return string; or raise a
<a class="reference internal" href="exceptions.html#LookupError" title="LookupError"><code class="xref py py-exc docutils literal notranslate"><span class="pre">LookupError</span></code></a> exception, to map the character to itself.</p>
<p>You can use <a class="reference internal" href="#str.maketrans" title="str.maketrans"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.maketrans()</span></code></a> to create a translation map from
character-to-character mappings in different formats.</p>
<p>See also the <a class="reference internal" href="codecs.html#module-codecs" title="codecs: Encode and decode data and streams."><code class="xref py py-mod docutils literal notranslate"><span class="pre">codecs</span></code></a> module for a more flexible approach to custom
character mappings.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.upper">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">upper</span></span><span class="sig-paren">(</span><span class="sig-paren">)</span><a class="headerlink" href="#str.upper" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string with all the cased characters <a class="footnote-reference brackets" href="#id15" id="id9">4</a> converted to
uppercase.  Note that <code class="docutils literal notranslate"><span class="pre">s.upper().isupper()</span></code> might be <code class="docutils literal notranslate"><span class="pre">False</span></code> if <code class="docutils literal notranslate"><span class="pre">s</span></code>
contains uncased characters or if the Unicode category of the resulting
character(s) is not “Lu” (Letter, uppercase), but e.g. “Lt” (Letter,
titlecase).</p>
<p>The uppercasing algorithm used is described in section 3.13 of the Unicode
Standard.</p>
</dd></dl>

<dl class="py method">
<dt class="sig sig-object py" id="str.zfill">
<span class="sig-prename descclassname"><span class="pre">str.</span></span><span class="sig-name descname"><span class="pre">zfill</span></span><span class="sig-paren">(</span><em class="sig-param"><span class="n"><span class="pre">width</span></span></em><span class="sig-paren">)</span><a class="headerlink" href="#str.zfill" title="Permalink to this definition">¶</a></dt>
<dd><p>Return a copy of the string left filled with ASCII <code class="docutils literal notranslate"><span class="pre">'0'</span></code> digits to
make a string of length <em>width</em>. A leading sign prefix (<code class="docutils literal notranslate"><span class="pre">'+'</span></code>/<code class="docutils literal notranslate"><span class="pre">'-'</span></code>)
is handled by inserting the padding <em>after</em> the sign character rather
than before. The original string is returned if <em>width</em> is less than
or equal to <code class="docutils literal notranslate"><span class="pre">len(s)</span></code>.</p>
<p>For example:</p>
<div class="highlight-python3 notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="s2">"42"</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="go">'00042'</span>
<span class="gp">&gt;&gt;&gt; </span><span class="s2">"-42"</span><span class="o">.</span><span class="n">zfill</span><span class="p">(</span><span class="mi">5</span><span class="p">)</span>
<span class="go">'-0042'</span>
</pre></div>
</div>
</dd></dl>

</section>
<section id="printf-style-string-formatting">
<span id="old-string-formatting"></span><h3><code class="docutils literal notranslate"><span class="pre">printf</span></code>-style String Formatting<a class="headerlink" href="#printf-style-string-formatting" title="Permalink to this headline">¶</a></h3>
<div class="admonition note" id="index-34">
<p class="admonition-title">Note</p>
<p>The formatting operations described here exhibit a variety of quirks that
lead to a number of common errors (such as failing to display tuples and
dictionaries correctly).  Using the newer <a class="reference internal" href="../reference/lexical_analysis.html#f-strings"><span class="std std-ref">formatted string literals</span></a>, the <a class="reference internal" href="#str.format" title="str.format"><code class="xref py py-meth docutils literal notranslate"><span class="pre">str.format()</span></code></a> interface, or <a class="reference internal" href="string.html#template-strings"><span class="std std-ref">template strings</span></a> may help avoid these errors.  Each of these
alternatives provides their own trade-offs and benefits of simplicity,
flexibility, and/or extensibility.</p>
</div>
<p>String objects have one unique built-in operation: the <code class="docutils literal notranslate"><span class="pre">%</span></code> operator (modulo).
This is also known as the string <em>formatting</em> or <em>interpolation</em> operator.
Given <code class="docutils literal notranslate"><span class="pre">format</span> <span class="pre">%</span> <span class="pre">values</span></code> (where <em>format</em> is a string), <code class="docutils literal notranslate"><span class="pre">%</span></code> conversion
specifications in <em>format</em> are replaced with zero or more elements of <em>values</em>.
The effect is similar to using the <code class="xref c c-func docutils literal notranslate"><span class="pre">sprintf()</span></code> in the C language.</p>
<p>If <em>format</em> requires a single argument, <em>values</em> may be a single non-tuple
object. <a class="footnote-reference brackets" href="#id16" id="id10">5</a>  Otherwise, <em>values</em> must be a tuple with exactly the number of
items specified by the format string, or a single mapping object (for example, a
dictionary).</p>
<p id="index-35">A conversion specifier contains two or more characters and has the following
components, which must occur in this order:</p>
<ol class="arabic simple">
<li><p>The <code class="docutils literal notranslate"><span class="pre">'%'</span></code> character, which marks the start of the specifier.</p></li>
<li><p>Mapping key (optional), consisting of a parenthesised sequence of characters
(for example, <code class="docutils literal notranslate"><span class="pre">(somename)</span></code>).</p></li>
<li><p>Conversion flags (optional), which affect the result of some conversion
types.</p></li>
<li><p>Minimum field width (optional).  If specified as an <code class="docutils literal notranslate"><span class="pre">'*'</span></code> (asterisk), the
actual width is read from the next element of the tuple in <em>values</em>, and the
object to convert comes after the minimum field width and optional precision.</p></li>
<li><p>Precision (optional), given as a <code class="docutils literal notranslate"><span class="pre">'.'</span></code> (dot) followed by the precision.  If
specified as <code class="docutils literal notranslate"><span class="pre">'*'</span></code> (an asterisk), the actual precision is read from the next
element of the tuple in <em>values</em>, and the value to convert comes after the
precision.</p></li>
<li><p>Length modifier (optional).</p></li>
<li><p>Conversion type.</p></li>
</ol>
<p>When the right argument is a dictionary (or other mapping type), then the
formats in the string <em>must</em> include a parenthesised mapping key into that
dictionary inserted immediately after the <code class="docutils literal notranslate"><span class="pre">'%'</span></code> character. The mapping key
selects the value to be formatted from the mapping.  For example:</p>
<div class="doctest highlight-default notranslate" style="position: relative;"><div class="highlight"><span class="copybutton" title="Hide the prompts and output" style="cursor: pointer; position: absolute; top: 0px; right: 0px; border-color: rgb(170, 204, 153); border-style: solid; border-width: 0.8px; color: rgb(170, 204, 153); font-family: monospace; padding-left: 0.2em; padding-right: 0.2em; border-radius: 0px 3px 0px 0px;">&gt;&gt;&gt;</span><pre><span></span><span class="gp">&gt;&gt;&gt; </span><span class="nb">print</span><span class="p">(</span><span class="s1">'</span><span class="si">%(language)s</span><span class="s1"> has </span><span class="si">%(number)03d</span><span class="s1"> quote types.'</span> <span class="o">%</span>
<span class="gp">... </span>      <span class="p">{</span><span class="s1">'language'</span><span class="p">:</span> <span class="s2">"Python"</span><span class="p">,</span> <span class="s2">"number"</span><span class="p">:</span> <span class="mi">2</span><span class="p">})</span>
<span class="go">Python has 002 quote types.</span>
</pre></div>
</div>
<p>In this case no <code class="docutils literal notranslate"><span class="pre">*</span></code> specifiers may occur in a format (since they require a
sequential parameter list).</p>
<p>The conversion flag characters are:</p>
<div class="responsive-table__container"><table class="docutils align-default" id="index-36">
<colgroup>
<col style="width: 12%">
<col style="width: 88%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Flag</p></th>
<th class="head"><p>Meaning</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'#'</span></code></p></td>
<td><p>The value conversion will use the “alternate form” (where defined
below).</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'0'</span></code></p></td>
<td><p>The conversion will be zero padded for numeric values.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'-'</span></code></p></td>
<td><p>The converted value is left adjusted (overrides the <code class="docutils literal notranslate"><span class="pre">'0'</span></code>
conversion if both are given).</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'</span> <span class="pre">'</span></code></p></td>
<td><p>(a space) A blank should be left before a positive number (or empty
string) produced by a signed conversion.</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'+'</span></code></p></td>
<td><p>A sign character (<code class="docutils literal notranslate"><span class="pre">'+'</span></code> or <code class="docutils literal notranslate"><span class="pre">'-'</span></code>) will precede the conversion
(overrides a “space” flag).</p></td>
</tr>
</tbody>
</table></div>
<p>A length modifier (<code class="docutils literal notranslate"><span class="pre">h</span></code>, <code class="docutils literal notranslate"><span class="pre">l</span></code>, or <code class="docutils literal notranslate"><span class="pre">L</span></code>) may be present, but is ignored as it
is not necessary for Python – so e.g. <code class="docutils literal notranslate"><span class="pre">%ld</span></code> is identical to <code class="docutils literal notranslate"><span class="pre">%d</span></code>.</p>
<p>The conversion types are:</p>
<div class="responsive-table__container"><table class="docutils align-default">
<colgroup>
<col style="width: 17%">
<col style="width: 74%">
<col style="width: 10%">
</colgroup>
<thead>
<tr class="row-odd"><th class="head"><p>Conversion</p></th>
<th class="head"><p>Meaning</p></th>
<th class="head"><p>Notes</p></th>
</tr>
</thead>
<tbody>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'d'</span></code></p></td>
<td><p>Signed integer decimal.</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'i'</span></code></p></td>
<td><p>Signed integer decimal.</p></td>
<td></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'o'</span></code></p></td>
<td><p>Signed octal value.</p></td>
<td><p>(1)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'u'</span></code></p></td>
<td><p>Obsolete type – it is identical to <code class="docutils literal notranslate"><span class="pre">'d'</span></code>.</p></td>
<td><p>(6)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'x'</span></code></p></td>
<td><p>Signed hexadecimal (lowercase).</p></td>
<td><p>(2)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'X'</span></code></p></td>
<td><p>Signed hexadecimal (uppercase).</p></td>
<td><p>(2)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'e'</span></code></p></td>
<td><p>Floating point exponential format (lowercase).</p></td>
<td><p>(3)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'E'</span></code></p></td>
<td><p>Floating point exponential format (uppercase).</p></td>
<td><p>(3)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'f'</span></code></p></td>
<td><p>Floating point decimal format.</p></td>
<td><p>(3)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'F'</span></code></p></td>
<td><p>Floating point decimal format.</p></td>
<td><p>(3)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'g'</span></code></p></td>
<td><p>Floating point format. Uses lowercase exponential
format if exponent is less than -4 or not less than
precision, decimal format otherwise.</p></td>
<td><p>(4)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'G'</span></code></p></td>
<td><p>Floating point format. Uses uppercase exponential
format if exponent is less than -4 or not less than
precision, decimal format otherwise.</p></td>
<td><p>(4)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'c'</span></code></p></td>
<td><p>Single character (accepts integer or single
character string).</p></td>
<td></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'r'</span></code></p></td>
<td><p>String (converts any Python object using
<a class="reference internal" href="functions.html#repr" title="repr"><code class="xref py py-func docutils literal notranslate"><span class="pre">repr()</span></code></a>).</p></td>
<td><p>(5)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'s'</span></code></p></td>
<td><p>String (converts any Python object using
<a class="reference internal" href="#str" title="str"><code class="xref py py-func docutils literal notranslate"><span class="pre">str()</span></code></a>).</p></td>
<td><p>(5)</p></td>
</tr>
<tr class="row-odd"><td><p><code class="docutils literal notranslate"><span class="pre">'a'</span></code></p></td>
<td><p>String (converts any Python object using
<a class="reference internal" href="functions.html#ascii" title="ascii"><code class="xref py py-func docutils literal notranslate"><span class="pre">ascii()</span></code></a>).</p></td>
<td><p>(5)</p></td>
</tr>
<tr class="row-even"><td><p><code class="docutils literal notranslate"><span class="pre">'%'</span></code></p></td>
<td><p>No argument is converted, results in a <code class="docutils literal notranslate"><span class="pre">'%'</span></code>
character in the result.</p></td>
<td></td>
</tr>
</tbody>
</table></div>
<p>Notes:</p>
<ol class="arabic">
<li><p>The alternate form causes a leading octal specifier (<code class="docutils literal notranslate"><span class="pre">'0o'</span></code>) to be
inserted before the first digit.</p></li>
<li><p>The alternate form causes a leading <code class="docutils literal notranslate"><span class="pre">'0x'</span></code> or <code class="docutils literal notranslate"><span class="pre">'0X'</span></code> (depending on whether
the <code class="docutils literal notranslate"><span class="pre">'x'</span></code> or <code class="docutils literal notranslate"><span class="pre">'X'</span></code> format was used) to be inserted before the first digit.</p></li>
<li><p>The alternate form causes the result to always contain a decimal point, even if
no digits follow it.</p>
<p>The precision determines the number of digits after the decimal point and
defaults to 6.</p>
</li>
<li><p>The alternate form causes the result to always contain a decimal point, and
trailing zeroes are not removed as they would otherwise be.</p>
<p>The precision determines the number of significant digits before and after the
decimal point and defaults to 6.</p>
</li>
<li><p>If precision is <code class="docutils literal notranslate"><span class="pre">N</span></code>, the output is truncated to <code class="docutils literal notranslate"><span class="pre">N</span></code> characters.</p></li>
<li><p>See <span class="target" id="index-37"></span><a class="pep reference external" href="https://peps.python.org/pep-0237/"><strong>PEP 237</strong></a>.</p></li>
</ol>
<p>Since Python strings have an explicit length, <code class="docutils literal notranslate"><span class="pre">%s</span></code> conversions do not assume
that <code class="docutils literal notranslate"><span class="pre">'\0'</span></code> is the end of the string.</p>
<div class="versionchanged">
<p><span class="versionmodified changed">Changed in version 3.1: </span><code class="docutils literal notranslate"><span class="pre">%f</span></code> conversions for numbers whose absolute value is over 1e50 are no
longer replaced by <code class="docutils literal notranslate"><span class="pre">%g</span></code> conversions.</p>
</div>
</section>
</section>

## Tasks
### 0. Print a list of integers
Write a function that prints all integers of a list.
* Prototype: `def print_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

```
guillaume@ubuntu:~/0x03$ cat 0-main.py
#!/usr/bin/python3
print_list_integer = __import__('0-print_list_integer').print_list_integer

my_list = [1, 2, 3, 4, 5]
print_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./0-main.py
1
2
3
4
5
guillaume@ubuntu:~/0x03$ 
```

### 1. Secure access to an element in a list
Write a function that retrieves an element from a list like in C.
* Prototype: `def element_at(my_list, idx):`
* If `idx` is negative, the function should return `None`
* If `idx` is out of range (> of number of element in `my_list`), the function should return `None`
* You are not allowed to import any module
* You are not allowed to use `try/except`

```
guillaume@ubuntu:~/0x03$ cat 1-main.py
#!/usr/bin/python3
element_at = __import__('1-element_at').element_at

my_list = [1, 2, 3, 4, 5]
idx = 3
print("Element at index {:d} is {}".format(idx, element_at(my_list, idx)))

guillaume@ubuntu:~/0x03$ ./1-main.py
Element at index 3 is 4
guillaume@ubuntu:~/0x03$ 
```

### 2. Replace element
Write a function that replaces an element of a list at a specific position (like in C).
* Prototype: `def replace_in_list(my_list, idx, element):`
* If `idx` is negative, the function should not modify anything, and returns the original list
* If `idx` is out of range (> of number of element in `my_list`), the function should not modify anything, and returns the original list
* You are not allowed to import any module
* You are not allowed to use `try/except`

```
guillaume@ubuntu:~/0x03$ cat 2-main.py
#!/usr/bin/python3
replace_in_list = __import__('2-replace_in_list').replace_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = replace_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./2-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 9, 5]
guillaume@ubuntu:~/0x03$ 
```
### 3. Print a list of integers... in reverse!
Write a function that prints all integers of a list, in reverse order.
* Prototype: `def print_reversed_list_integer(my_list=[]):`
* Format: one integer per line. See example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

```
guillaume@ubuntu:~/0x03$ cat 3-main.py
#!/usr/bin/python3
print_reversed_list_integer = __import__('3-print_reversed_list_integer').print_reversed_list_integer

my_list = [1, 2, 3, 4, 5]
print_reversed_list_integer(my_list)

guillaume@ubuntu:~/0x03$ ./3-main.py
5
4
3
2
1
guillaume@ubuntu:~/0x03$ 
```

### 4. Replace in a copy
Write a function that replaces an element in a list at a specific position without modifying the original list (like in C).
* Prototype: `def new_in_list(my_list, idx, element):`
* If `idx` is negative, the function should return a copy of the original `list`
* If `idx` is out of range (> of number of element in `my_list`), the function should return a copy of the original `list`
* You are not allowed to import any module
* You are not allowed to use `try/except`

```
guillaume@ubuntu:~/0x03$ cat 4-main.py
#!/usr/bin/python3
new_in_list = __import__('4-new_in_list').new_in_list

my_list = [1, 2, 3, 4, 5]
idx = 3
new_element = 9
new_list = new_in_list(my_list, idx, new_element)

print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./4-main.py
[1, 2, 3, 9, 5]
[1, 2, 3, 4, 5]
guillaume@ubuntu:~/0x03$ 
```

#### Resources
* [How to copy a list in Python](https://flexiple.com/python/python-copy-list/)
### 5. Can you C me now?
Write a function that removes all characters `c` and `C` from a string.
* Prototype: `def no_c(my_string):`
* The function should return the new string
* You are not allowed to import any module
* You are not allowed to use `str.replace()`

```
guillaume@ubuntu:~/0x03$ cat 5-main.py
#!/usr/bin/env python3
no_c = __import__('5-no_c').no_c

print(no_c("Best School"))
print(no_c("Chicago"))
print(no_c("C is fun!"))

guillaume@ubuntu:~/0x03$ ./5-main.py
Best Shool
hiago
 is fun!
guillaume@ubuntu:~/0x03$ 
```

### 6. Lists of lists = Matrix
Write a function that prints a matrix of integers.
* Prototype: `def print_matrix_integer(matrix=[[]]):`
* Format: see example
* You are not allowed to import any module
* You can assume that the list only contains integers
* You are not allowed to cast integers into strings
* You have to use `str.format()` to print integers

```
guillaume@ubuntu:~/0x03$ cat 6-main.py
#!/usr/bin/python3
print_matrix_integer = __import__('6-print_matrix_integer').print_matrix_integer

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()

guillaume@ubuntu:~/0x03$ ./6-main.py | cat -e
1 2 3$
4 5 6$
7 8 9$
--$
$
guillaume@ubuntu:~/0x03$ 
```

#### Resources
* [Multi-dimensional lists in Python](https://www.geeksforgeeks.org/multi-dimensional-list-sin-python/)
### 7. Tuples addition
Write a function that adds 2 tuples.
* Prototype: `def add_tuple(tuple_a=(), tuple_b=()):`
* Returns a tuple with 2 integers:
* The first element should be the addition of the first element of each argument
* The second element should be the addition of the second element of each argument
* You are not allowed to import any module
* You can assume that the two tuples will only contain integers
* If a tuple is smaller than 2, use the value `0` for each missing integer
* If a tuple is bigger than 2, use only the first 2 integers

```
guillaume@ubuntu:~/0x03$ cat 7-main.py
#!/usr/bin/python3
add_tuple = __import__('7-add_tuple').add_tuple

tuple_a = (1, 89)
tuple_b = (88, 11)
new_tuple = add_tuple(tuple_a, tuple_b)
print(new_tuple)

print(add_tuple(tuple_a, (1, )))
print(add_tuple(tuple_a, ()))

guillaume@ubuntu:~/0x03$ ./7-main.py
(89, 100)
(2, 89)
(1, 89)
guillaume@ubuntu:~/0x03$ 
```

### 8. More returns!
Write a function that returns a tuple with the length of a string and its first character.

* Prototype: `def multiple_returns(sentence):`
* If the sentence is empty, the first character should be equal to `None`
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x03$ cat 8-main.py
#!/usr/bin/python3
multiple_returns = __import__('8-multiple_returns').multiple_returns

sentence = "At school, I learnt C!"
length, first = multiple_returns(sentence)
print("Length: {:d} - First character: {}".format(length, first))

guillaume@ubuntu:~/0x03$ ./8-main.py
Length: 22 - First character: A
guillaume@ubuntu:~/0x03$ 
```

### 9. Find the max
Write a function that finds the biggest integer of a list.
* Prototype: `def max_integer(my_list=[]):`
* If the list is empty, return `None`
* You can assume that the list only contains integers
* You are not allowed to import any module
* You are not allowed to use the builtin `max()`

```
guillaume@ubuntu:~/0x03$ cat 9-main.py
#!/usr/bin/python3
max_integer = __import__('9-max_integer').max_integer

my_list = [1, 90, 2, 13, 34, 5, -13, 3]
max_value = max_integer(my_list)
print("Max: {}".format(max_value))

guillaume@ubuntu:~/0x03$ ./9-main.py
Max: 90
guillaume@ubuntu:~/0x03$ 
```

### 10. Only by 2
Write a function that finds all multiples of 2 in a list.
* Prototype: `def divisible_by_2(my_list=[]):`
* Return a new list with `True` or `False`, depending on whether the integer at the same position in the original list is a multiple of 2
* The new list should have the same size as the original list
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x03$ cat 10-main.py
#!/usr/bin/python3
divisible_by_2 = __import__('10-divisible_by_2').divisible_by_2

my_list = [0, 1, 2, 3, 4, 5, 6]
list_result = divisible_by_2(my_list)

i = 0
while i < len(list_result):
    print("{:d} {:s} divisible by 2".format(my_list[i], "is" if list_result[i] else "is not"))
    i += 1

guillaume@ubuntu:~/0x03$ ./10-main.py
0 is divisible by 2
1 is not divisible by 2
2 is divisible by 2
3 is not divisible by 2
4 is divisible by 2
5 is not divisible by 2
6 is divisible by 2
guillaume@ubuntu:~/0x03$ 
```

### 11. Delete at
Write a function that deletes the item at a specific position in a list.

* Prototype: `def delete_at(my_list=[], idx=0):`
* If `idx` is negative or out of range, nothing change (returns the same list)
* You are not allowed to use `pop()`
* You are not allowed to import any module
```
guillaume@ubuntu:~/0x03$ cat 11-main.py
#!/usr/bin/python3
delete_at = __import__('11-delete_at').delete_at

my_list = [1, 2, 3, 4, 5]
idx = 3
new_list = delete_at(my_list, idx)
print(new_list)
print(my_list)

guillaume@ubuntu:~/0x03$ ./11-main.py
[1, 2, 3, 5]
[1, 2, 3, 5]
guillaume@ubuntu:~/0x03$ 
```

### 12. Switch
Complete the source code in order to switch value of `a` and `b`
* You can find the source code [here](https://github.com/holbertonschool/0x03.py/blob/master/12-switch_py)
* Your code should be inserted where the comment is (line 4)
* Your program should be exactly 5 lines long
```
guillaume@ubuntu:~/py/0x03$ ./12-switch.py
a=10 - b=89
guillaume@ubuntu:~/py/0x03$ wc -l 12-switch.py
5 12-switch.py
guillaume@ubuntu:~/py/0x03$ 
```

### 13. Linked list palindrome
**Technical interview preparation:**
* You are not allowed to google anything
* Whiteboard first

Write a function in C that checks if a singly linked list is a palindrome.
* Prototype: `int is_palindrome(listint_t **head);`
* Return: `0` if it is not a palindrome, `1` if it is a palindrome
* An empty list is considered a palindrome
```
carrie@ubuntu:0x03$ cat lists.h 
#ifndef LISTS_H
#define LISTS_H

/**
 * struct listint_s - singly linked list
 * @n: integer
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 * for project
 */
typedef struct listint_s
{
    int n;
    struct listint_s *next;
} listint_t;

size_t print_listint(const listint_t *h);
listint_t *add_nodeint_end(listint_t **head, const int n);
void free_listint(listint_t *head);

int is_palindrome(listint_t **head);

#endif /* LISTS_H */
carrie@ubuntu:0x03$
```
```
carrie@ubuntu:0x03$ cat linked_lists.c 
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * print_listint - prints all elements of a listint_t list
 * @h: pointer to head of list
 * Return: number of nodes
 */
size_t print_listint(const listint_t *h)
{
    const listint_t *current;
    unsigned int n; /* number of nodes */

    current = h;
    n = 0;
    while (current != NULL)
    {
        printf("%i\n", current->n);
        current = current->next;
        n++;
    }

    return (n);
}

/**
 * add_nodeint_end - adds a new node at the end of a listint_t list
 * @head: pointer to pointer of first node of listint_t list
 * @n: integer to be included in new node
 * Return: address of the new element or NULL if it fails
 */
listint_t *add_nodeint_end(listint_t **head, const int n)
{
    listint_t *new;
    listint_t *current;

    current = *head;

    new = malloc(sizeof(listint_t));
    if (new == NULL)
        return (NULL);

    new->n = n;
    new->next = NULL;

    if (*head == NULL)
        *head = new;
    else
    {
        while (current->next != NULL)
            current = current->next;
        current->next = new;
    }

    return (new);
}

/**
 * free_listint - frees a listint_t list
 * @head: pointer to list to be freed
 * Return: void
 */
void free_listint(listint_t *head)
{
    listint_t *current;

    while (head != NULL)
    {
        current = head;
        head = head->next;
        free(current);
    }
}
carrie@ubuntu:0x03$
```
```
carrie@ubuntu:0x03$ cat 13-main.c
#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * main - check the code for
 *
 * Return: Always 0.
 */
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 50);
    add_nodeint_end(&head, 972);
    add_nodeint_end(&head, 17);
    add_nodeint_end(&head, 1);
    print_listint(head);

    if (is_palindrome(&head) == 1)
        printf("Linked list is a palindrome\n");
    else
        printf("Linked list is not a palindrome\n");

    free_listint(head);

    return (0);
}
carrie@ubuntu:0x03$
```
```
carrie@ubuntu:0x03$ gcc -Wall -Werror -Wextra -pedantic 13-main.c linked_lists.c 13-is_palindrome.c -o palindrome
carrie@ubuntu:0x03$ ./palindrome
1
17
972
50
98
98
50
972
17
1
Linked list is a palindrome
carrie@ubuntu:0x03$
```
### 14. CPython #0: Python lists
CPython is the reference implementation of the Python programming language. Written in C, CPython is the default and most widely used implementation of the language.
Since we now know a bit of C, we can look at what is happening under the hood of Python. Let’s have fun with Python and C, and let’s look at what makes Python so easy to use.
* All your files will be interpreted/compiled on Ubuntu 14.04 LTS

Create a C function that prints some basic info about Python lists.
* Prototype: `void print_python_list_info(PyObject *p);`
* Format: see example
* Python version: 3.4
* Your shared library will be compiled with this command line: ```gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c```
* OS: `Ubuntu 14.04 LTS`
* Start by reading:
	* listobject.h
	* object.h
	* [Common Object Structures](https://docs.python.org/3/c-api/structures.html)
	* [List Objects](https://docs.python.org/3/c-api/list.html)

```
julien@ubuntu:~/CPython$ gcc -Wall -Werror -Wextra -pedantic -std=c99 -shared -Wl,-soname,PyList -o libPyList.so -fPIC -I/usr/include/python3.4 100-print_python_list_info.c
julien@ubuntu:~/CPython$ cat 100-test_lists.py 
import ctypes

lib = ctypes.CDLL('./libPyList.so')
lib.print_python_list_info.argtypes = [ctypes.py_object]
l = ['hello', 'World']
lib.print_python_list_info(l)
del l[1]
lib.print_python_list_info(l)
l = l + [4, 5, 6.0, (9, 8), [9, 8, 1024], "My string"]
lib.print_python_list_info(l)
l = []
lib.print_python_list_info(l)
l.append(0)
lib.print_python_list_info(l)
l.append(1)
l.append(2)
l.append(3)
l.append(4)
lib.print_python_list_info(l)
l.pop()
lib.print_python_list_info(l)
julien@ubuntu:~/CPython$ python3 100-test_lists.py
[*] Size of the Python List = 2
[*] Allocated = 2
Element 0: str
Element 1: str
[*] Size of the Python List = 1
[*] Allocated = 2
Element 0: str
[*] Size of the Python List = 7
[*] Allocated = 7
Element 0: str
Element 1: int
Element 2: int
Element 3: float
Element 4: tuple
Element 5: list
Element 6: str
[*] Size of the Python List = 0
[*] Allocated = 0
[*] Size of the Python List = 1
[*] Allocated = 4
Element 0: int
[*] Size of the Python List = 5
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
Element 4: int
[*] Size of the Python List = 4
[*] Allocated = 8
Element 0: int
Element 1: int
Element 2: int
Element 3: int
julien@CPython:~/CPython$
```
***
## Author
* **[THE_QUADZILLA](https://github.com/nyaberi-mayaka)**
***