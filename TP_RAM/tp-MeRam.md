Aunque tengan los mismos datos, están en posiciones distintas de memoria.

<pre class="overflow-visible! px-0!" data-start="1146" data-end="1178"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼt">dog1</span><span></span><span class="ͼn">===</span><span></span><span class="ͼt">dog2</span><span></span><span class="ͼl">// false</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

### 🔹 Diferencia entre primitivo y objeto

<pre class="overflow-visible! px-0!" data-start="1229" data-end="1297"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">const</span><span></span><span class="ͼt">nombre</span><span></span><span class="ͼn">=</span><span></span><span class="ͼr">"fede"</span><span>;</span><br/><span class="ͼn">const</span><span></span><span class="ͼt">nombre2</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">String</span><span>(</span><span class="ͼr">"fede"</span><span>);</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

* `"fede"` → es un valor primitivo (más liviano, se guarda en stack)
* `new String("fede")` → es un objeto (se guarda en heap)

No son iguales:

<pre class="overflow-visible! px-0!" data-start="1444" data-end="1492"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼr">"fede"</span><span></span><span class="ͼn">===</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">String</span><span>(</span><span class="ͼr">"fede"</span><span>) </span><span class="ͼl">// false</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

👉 En general, no conviene usar `new String`, `new Number` o `new Boolean`.

---

## 🧩 Esquema: Stack vs Heap

<pre class="overflow-visible! px-0!" data-start="1606" data-end="1819"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute end-1.5 top-1 z-2 md:end-2 md:top-1"></div><div class="relative"><div class="pe-11 pt-3"><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span>STACK (rápido)             HEAP (dinámico)</span><br/><br/><span>nombre → "fede"           { name: "Rex" }</span><br/><span>edad → 30                 { name: "Rex" }</span><br/><br/><span>dog1 → referencia ─────▶ objeto Dog</span><br/><span>dog2 → referencia ─────▶ otro objeto Dog</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

* Stack: variables primitivas y referencias
* Heap: objetos, arrays, instancias

---

## 💻 Parte 2 – Problemas en el código

Código original:

<pre class="overflow-visible! px-0!" data-start="1965" data-end="2154"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">const</span><span></span><span class="ͼt">nombre</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">String</span><span>(</span><span class="ͼr">"Juan"</span><span>);</span><br/><span class="ͼn">const</span><span></span><span class="ͼt">apellido</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">String</span><span>(</span><span class="ͼr">"Perez"</span><span>);</span><br/><br/><span class="ͼn">const</span><span></span><span class="ͼt">nombreCompleto</span><span></span><span class="ͼn">=</span><span></span><span class="ͼt">nombre</span><span></span><span class="ͼn">+</span><span></span><span class="ͼt">apellido</span><span>;</span><br/><br/><span class="ͼn">const</span><span></span><span class="ͼt">edad</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">Number</span><span>(</span><span class="ͼq">30</span><span>);</span><br/><span class="ͼn">const</span><span></span><span class="ͼt">activo</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">Boolean</span><span>(</span><span class="ͼq">true</span><span>);</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### ❌ Problemas detectados:

* Uso innecesario de objetos
* Mayor consumo de memoria
* Puede generar errores en comparaciones
* Menor rendimiento

---

### ✅ Versión corregida:

<pre class="overflow-visible! px-0!" data-start="2334" data-end="2474"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">const</span><span></span><span class="ͼt">nombre</span><span></span><span class="ͼn">=</span><span></span><span class="ͼr">"Juan"</span><span>;</span><br/><span class="ͼn">const</span><span></span><span class="ͼt">apellido</span><span></span><span class="ͼn">=</span><span></span><span class="ͼr">"Perez"</span><span>;</span><br/><br/><span class="ͼn">const</span><span></span><span class="ͼt">nombreCompleto</span><span></span><span class="ͼn">=</span><span></span><span class="ͼt">nombre</span><span></span><span class="ͼn">+</span><span></span><span class="ͼt">apellido</span><span>;</span><br/><br/><span class="ͼn">const</span><span></span><span class="ͼt">edad</span><span></span><span class="ͼn">=</span><span></span><span class="ͼq">30</span><span>;</span><br/><span class="ͼn">const</span><span></span><span class="ͼt">activo</span><span></span><span class="ͼn">=</span><span></span><span class="ͼq">true</span><span>;</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🔧 Parte 3 – Refactor

Código original:

<pre class="overflow-visible! px-0!" data-start="2525" data-end="2609"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">class</span><span></span><span class="ͼs">User</span><span> {</span><br/><span>  constructor(</span><span class="ͼt">name</span><span>) {</span><br/><span></span><span class="ͼq">this</span><span class="ͼn">.</span><span>name </span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">String</span><span>(</span><span class="ͼt">name</span><span>);</span><br/><span>  }</span><br/><span>}</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

### ❌ Problema:

Se está creando un objeto innecesario con `new String`.

---

### ✅ Versión mejorada:

<pre class="overflow-visible! px-0!" data-start="2714" data-end="2786"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">class</span><span></span><span class="ͼs">User</span><span> {</span><br/><span>  constructor(</span><span class="ͼt">name</span><span>) {</span><br/><span></span><span class="ͼq">this</span><span class="ͼn">.</span><span>name </span><span class="ͼn">=</span><span></span><span class="ͼt">name</span><span>;</span><br/><span>  }</span><br/><span>}</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Esto reduce el uso de memoria y simplifica el código.

---

## 🚀 Parte 4 – Instancias y duplicación

<pre class="overflow-visible! px-0!" data-start="2890" data-end="2957"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">const</span><span></span><span class="ͼt">dog1</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">Dog</span><span>(</span><span class="ͼr">"Rex"</span><span>);</span><br/><span class="ͼn">const</span><span></span><span class="ͼt">dog2</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">Dog</span><span>(</span><span class="ͼr">"Rex"</span><span>);</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Cada instancia:

* Es independiente
* Ocupa su propio espacio en memoria

Si quiero evitar duplicados, puedo usar una especie de "cache":

<pre class="overflow-visible! px-0!" data-start="3097" data-end="3228"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">const</span><span></span><span class="ͼt">dogs</span><span></span><span class="ͼn">=</span><span> {};</span><br/><br/><span class="ͼn">function</span><span></span><span class="ͼt">getDog</span><span>(</span><span class="ͼt">name</span><span>) {</span><br/><span></span><span class="ͼn">if</span><span> (</span><span class="ͼn">!</span><span class="ͼt">dogs</span><span>[</span><span class="ͼt">name</span><span>]) {</span><br/><span></span><span class="ͼt">dogs</span><span>[</span><span class="ͼt">name</span><span>] </span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">Dog</span><span>(</span><span class="ͼt">name</span><span>);</span><br/><span>  }</span><br/><span></span><span class="ͼn">return</span><span></span><span class="ͼt">dogs</span><span>[</span><span class="ͼt">name</span><span>];</span><br/><span>}</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

---

## 🧠 Parte 5 – Singleton

Objetivo: que exista una sola instancia de una clase.

<pre class="overflow-visible! px-0!" data-start="3317" data-end="3642"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼn">class</span><span></span><span class="ͼs">Config</span><span> {</span><br/><span>  constructor(</span><span class="ͼt">url</span><span>, </span><span class="ͼt">port</span><span>) {</span><br/><span></span><span class="ͼn">if</span><span> (</span><span class="ͼt">Config</span><span class="ͼn">.</span><span>instance) {</span><br/><span></span><span class="ͼn">return</span><span></span><span class="ͼt">Config</span><span class="ͼn">.</span><span>instance;</span><br/><span>    }</span><br/><br/><span></span><span class="ͼq">this</span><span class="ͼn">.</span><span>url </span><span class="ͼn">=</span><span></span><span class="ͼt">url</span><span>;</span><br/><span></span><span class="ͼq">this</span><span class="ͼn">.</span><span>port </span><span class="ͼn">=</span><span></span><span class="ͼt">port</span><span>;</span><br/><br/><span></span><span class="ͼt">Config</span><span class="ͼn">.</span><span>instance </span><span class="ͼn">=</span><span></span><span class="ͼq">this</span><span>;</span><br/><span>  }</span><br/><span>}</span><br/><br/><span class="ͼn">const</span><span></span><span class="ͼt">config1</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">Config</span><span>(</span><span class="ͼr">"localhost"</span><span>, </span><span class="ͼq">3000</span><span>);</span><br/><span class="ͼn">const</span><span></span><span class="ͼt">config2</span><span></span><span class="ͼn">=</span><span></span><span class="ͼn">new</span><span></span><span class="ͼt">Config</span><span>(</span><span class="ͼr">"otro"</span><span>, </span><span class="ͼq">8080</span><span>);</span><br/><br/><span class="ͼt">console</span><span class="ͼn">.</span><span>log(</span><span class="ͼt">config1</span><span></span><span class="ͼn">===</span><span></span><span class="ͼt">config2</span><span>); </span><span class="ͼl">// true</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

👉 Todos usan la misma instancia.

---

## Uso de memoria en Node.js

<pre class="overflow-visible! px-0!" data-start="3725" data-end="3770"><div class="relative w-full mt-4 mb-1"><div class=""><div class="relative"><div class="h-full min-h-0 min-w-0"><div class="h-full min-h-0 min-w-0"><div class="border border-token-border-light border-radius-3xl corner-superellipse/1.1 rounded-3xl"><div class="h-full w-full border-radius-3xl bg-token-bg-elevated-secondary corner-superellipse/1.1 overflow-clip rounded-3xl lxnfua_clipPathFallback"><div class="pointer-events-none absolute inset-x-4 top-12 bottom-4"><div class="pointer-events-none sticky z-40 shrink-0 z-1!"><div class="sticky bg-token-border-light"></div></div></div><div class="relative"><div class=""><div class="relative z-0 flex max-w-full"><div id="code-block-viewer" dir="ltr" class="q9tKkq_viewer cm-editor z-10 light:cm-light dark:cm-light flex h-full w-full flex-col items-stretch ͼk ͼy"><div class="cm-scroller"><div class="cm-content q9tKkq_readonly"><span class="ͼt">console</span><span class="ͼn">.</span><span>log(</span><span class="ͼt">process</span><span class="ͼn">.</span><span>memoryUsage());</span></div></div></div></div></div></div></div></div></div></div><div class=""><div class=""></div></div></div></div></div></pre>

Esto muestra información sobre el uso de memoria del proceso, como:

* memoria total
* memoria usada
* heap

---

## 🧾 Conclusión

* Evitar crear objetos innecesarios (`new String`, etc.)
* Entender que cada `new` ocupa memoria nueva
* Usar tipos primitivos siempre que sea posible
* Controlar la creación de instancias si hay duplicación
* Aplicar patrones como Singleton cuando sea necesario
