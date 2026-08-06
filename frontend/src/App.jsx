import { useState } from 'react'
import './App.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://127.0.0.1:8000'

export default function App() {
  const [file, setFile] = useState(null)
  const [question, setQuestion] = useState('')
  const [messages, setMessages] = useState([])
  const [status, setStatus] = useState('Upload a PDF to begin.')
  const [busy, setBusy] = useState(false)

  const readError = async (response) => {
    const body = await response.json().catch(() => ({}))
    return body.detail || body.message || 'Something went wrong. Please try again.'
  }

  const upload = async (event) => {
    event.preventDefault()
    if (!file) return setStatus('Choose a PDF file first.')
    setBusy(true); setStatus('Indexing your PDF…')
    const data = new FormData(); data.append('file', file)
    try {
      const response = await fetch(`${API_URL}/upload`, { method: 'POST', body: data })
      if (!response.ok) throw new Error(await readError(response))
      const result = await response.json()
      setStatus(`${result.filename} is ready (${result.chunks} sections indexed).`)
      setMessages([])
    } catch (error) { setStatus(error.message) } finally { setBusy(false) }
  }

  const ask = async (event) => {
    event.preventDefault()
    const text = question.trim()
    if (!text || busy) return
    setQuestion(''); setMessages((items) => [...items, { role: 'You', text }]); setBusy(true)
    try {
      const response = await fetch(`${API_URL}/chat`, { method: 'POST', headers: { 'Content-Type': 'application/json' }, body: JSON.stringify({ question: text }) })
      if (!response.ok) throw new Error(await readError(response))
      const result = await response.json()
      setMessages((items) => [...items, { role: 'DocMind', text: result.answer }])
    } catch (error) { setMessages((items) => [...items, { role: 'DocMind', text: error.message, error: true }]) } finally { setBusy(false) }
  }

  return <main className="app"><section className="card">
    <header><span className="mark">D</span><div><h1>DocMind AI</h1><p>Chat with the information in your PDF.</p></div></header>
    <form className="upload" onSubmit={upload}><input aria-label="Choose PDF" type="file" accept="application/pdf,.pdf" onChange={(e) => setFile(e.target.files?.[0] || null)} /><button disabled={busy}>{busy ? 'Working…' : 'Upload & index'}</button></form>
    <p className="status" aria-live="polite">{status}</p>
    <div className="chat" aria-live="polite">{messages.length ? messages.map((message, index) => <article className={`message ${message.error ? 'error' : ''}`} key={index}><strong>{message.role}</strong><p>{message.text}</p></article>) : <p className="empty">Your answers will appear here after you upload a document.</p>}</div>
    <form className="ask" onSubmit={ask}><input value={question} onChange={(e) => setQuestion(e.target.value)} placeholder="Ask a question about the PDF…" disabled={busy} /><button disabled={busy}>Send</button></form>
  </section></main>
}
