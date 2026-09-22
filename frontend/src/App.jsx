import { useState, useEffect } from 'react'
import './index.css'

const API_URL = import.meta.env.VITE_API_URL || 'http://localhost:8000'

function App() {
  const [workers, setWorkers] = useState([])
  const [sites, setSites] = useState([])
  const [newWorkerName, setNewWorkerName] = useState('')
  const [newSiteName, setNewSiteName] = useState('')

  useEffect(() => {
    fetchWorkers()
    fetchSites()
  }, [])

  const fetchWorkers = async () => {
    try {
      const res = await fetch(`${API_URL}/workers/`)
      if (res.ok) {
        const data = await res.json()
        setWorkers(data)
      }
    } catch (err) {
      console.error("Failed to fetch workers", err)
    }
  }

  const fetchSites = async () => {
    try {
      const res = await fetch(`${API_URL}/sites/`)
      if (res.ok) {
        const data = await res.json()
        setSites(data)
      }
    } catch (err) {
      console.error("Failed to fetch sites", err)
    }
  }

  const handleAddWorker = async (e) => {
    e.preventDefault()
    if (!newWorkerName) return
    try {
      const res = await fetch(`${API_URL}/workers/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newWorkerName, is_active: true })
      })
      if (res.ok) {
        setNewWorkerName('')
        fetchWorkers()
      }
    } catch (err) {
      console.error(err)
    }
  }

  const handleAddSite = async (e) => {
    e.preventDefault()
    if (!newSiteName) return
    try {
      const res = await fetch(`${API_URL}/sites/`, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ name: newSiteName, requires_specialist: false })
      })
      if (res.ok) {
        setNewSiteName('')
        fetchSites()
      }
    } catch (err) {
      console.error(err)
    }
  }

  return (
    <div className="app-container">
      <header className="header">
        <h1>Roster Management</h1>
        <p>Dynamic worker and site assignment system</p>
      </header>

      <div className="grid">
        {/* Workers Card */}
        <div className="card">
          <h2>Workers</h2>
          <form onSubmit={handleAddWorker} className="form-group" style={{ display: 'flex', gap: '0.5rem' }}>
            <input 
              type="text" 
              className="input" 
              placeholder="New worker name..." 
              value={newWorkerName}
              onChange={e => setNewWorkerName(e.target.value)}
            />
            <button type="submit" className="btn">Add</button>
          </form>
          <ul className="list">
            {workers.map(w => (
              <li key={w.id} className="list-item">
                <span>{w.name}</span>
                <span className={`badge ${w.is_active ? 'badge-success' : ''}`}>
                  {w.is_active ? 'Active' : 'Inactive'}
                </span>
              </li>
            ))}
            {workers.length === 0 && <li className="list-item" style={{color: 'var(--text-muted)'}}>No workers found.</li>}
          </ul>
        </div>

        {/* Sites Card */}
        <div className="card">
          <h2>Sites</h2>
          <form onSubmit={handleAddSite} className="form-group" style={{ display: 'flex', gap: '0.5rem' }}>
            <input 
              type="text" 
              className="input" 
              placeholder="New site name..." 
              value={newSiteName}
              onChange={e => setNewSiteName(e.target.value)}
            />
            <button type="submit" className="btn">Add</button>
          </form>
          <ul className="list">
            {sites.map(s => (
              <li key={s.id} className="list-item">
                <span>{s.name}</span>
              </li>
            ))}
            {sites.length === 0 && <li className="list-item" style={{color: 'var(--text-muted)'}}>No sites found.</li>}
          </ul>
        </div>
      </div>
    </div>
  )
}

export default App
