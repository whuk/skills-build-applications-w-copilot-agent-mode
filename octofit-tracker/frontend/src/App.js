import './App.css';
import { Navigate, NavLink, Route, Routes } from 'react-router-dom';

import Activities from './components/Activities';
import Leaderboard from './components/Leaderboard';
import Teams from './components/Teams';
import Users from './components/Users';
import Workouts from './components/Workouts';

function App() {
  const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
  const apiBaseUrl = codespaceName
    ? `https://${codespaceName}-8000.app.github.dev/api`
    : 'http://localhost:8000/api';

  return (
    <main className="app-shell py-4">
      <div className="container">
        <div className="card shadow-sm mb-4">
          <div className="card-body">
            <div className="d-flex align-items-start gap-3 mb-2">
              <img
                src="/octofitapp-small.png"
                alt="OctoFit logo"
                className="app-logo"
                width="56"
                height="56"
              />
              <div>
                <h1 className="h2 mb-2 app-title">OctoFit Tracker Dashboard</h1>
                <p className="mb-1 app-subtitle">
                  Backend API endpoint:{' '}
                  <a className="link-primary app-link" href={apiBaseUrl} target="_blank" rel="noreferrer">
                    {apiBaseUrl}
                  </a>
                </p>
                <p className="small text-muted mb-0">Use the menu below to browse each REST resource.</p>
              </div>
            </div>
          </div>
        </div>

        <nav className="nav nav-pills flex-wrap gap-2 mb-4">
          <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/users">
            Users
          </NavLink>
          <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/teams">
            Teams
          </NavLink>
          <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/activities">
            Activities
          </NavLink>
          <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/leaderboard">
            Leaderboard
          </NavLink>
          <NavLink className={({ isActive }) => `nav-link${isActive ? ' active' : ''}`} to="/workouts">
            Workouts
          </NavLink>
        </nav>

        <Routes>
          <Route path="/" element={<Navigate to="/users" replace />} />
          <Route path="/users" element={<Users />} />
          <Route path="/teams" element={<Teams />} />
          <Route path="/activities" element={<Activities />} />
          <Route path="/leaderboard" element={<Leaderboard />} />
          <Route path="/workouts" element={<Workouts />} />
          <Route path="*" element={<Navigate to="/users" replace />} />
        </Routes>
      </div>
    </main>
  );
}

export default App;
