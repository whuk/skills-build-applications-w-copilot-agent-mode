import { useEffect, useState } from 'react';

function Activities() {
  const [items, setItems] = useState([]);
  const [error, setError] = useState('');
  const [query, setQuery] = useState('');
  const [selected, setSelected] = useState(null);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const codespaceName = process.env.REACT_APP_CODESPACE_NAME;
    const apiBaseUrl = codespaceName
      ? `https://${codespaceName}-8000.app.github.dev/api`
      : 'http://localhost:8000/api';

    const load = async () => {
      try {
        const endpoint = `${apiBaseUrl}/activities/`;
        console.log('Activities endpoint:', endpoint);
        const response = await fetch(endpoint);
        if (!response.ok) {
          throw new Error(`HTTP ${response.status}`);
        }
        const data = await response.json();
        console.log('Activities fetched data:', data);
        const normalizedItems = Array.isArray(data)
          ? data
          : Array.isArray(data?.results)
            ? data.results
            : [];
        console.log('Activities API payload:', data);
        console.log('Activities normalized items:', normalizedItems);
        setItems(normalizedItems);
      } catch (err) {
        setError(String(err));
      } finally {
        setLoading(false);
      }
    };

    load();
  }, []);

  if (loading) return <p>Loading activities...</p>;

  const filteredItems = items.filter((item) => {
    const haystack = `${item.activity_type} ${item.duration_minutes} ${item.calories_burned} ${item.user}`.toLowerCase();
    return haystack.includes(query.toLowerCase());
  });

  return (
    <section className="card shadow-sm">
      <div className="card-body">
        <div className="d-flex justify-content-between align-items-center mb-3">
          <h2 className="h4 mb-0">Activities</h2>
          <span className="badge text-bg-primary">{filteredItems.length}</span>
        </div>

        <form className="row g-2 mb-3" onSubmit={(event) => event.preventDefault()}>
          <div className="col-sm-9 col-md-10">
            <input
              className="form-control"
              type="search"
              placeholder="Search by activity type or user"
              value={query}
              onChange={(event) => setQuery(event.target.value)}
            />
          </div>
          <div className="col-sm-3 col-md-2 d-grid">
            <button className="btn btn-outline-secondary" type="button" onClick={() => setQuery('')}>
              Clear
            </button>
          </div>
        </form>

        {error && <p className="text-danger">Activities API error: {error}</p>}

        <div className="table-responsive">
          <table className="table table-striped table-hover align-middle">
            <thead className="table-light">
              <tr>
                <th>ID</th>
                <th>Type</th>
                <th>Duration (min)</th>
                <th>Calories</th>
                <th>User</th>
                <th className="text-end">Action</th>
              </tr>
            </thead>
            <tbody>
              {filteredItems.map((item) => (
                <tr key={item.id}>
                  <td>{item.id}</td>
                  <td>{item.activity_type}</td>
                  <td>{item.duration_minutes}</td>
                  <td>{item.calories_burned}</td>
                  <td>{item.user}</td>
                  <td className="text-end">
                    <button className="btn btn-sm btn-primary" type="button" onClick={() => setSelected(item)}>
                      Details
                    </button>
                  </td>
                </tr>
              ))}
            </tbody>
          </table>
        </div>
      </div>

      {selected && (
        <>
          <div className="modal fade show d-block" tabIndex="-1" role="dialog" aria-modal="true">
            <div className="modal-dialog modal-dialog-centered modal-lg">
              <div className="modal-content">
                <div className="modal-header">
                  <h3 className="h5 modal-title mb-0">Activity Detail</h3>
                  <button className="btn-close" type="button" onClick={() => setSelected(null)}></button>
                </div>
                <div className="modal-body">
                  <pre className="json-preview mb-0">{JSON.stringify(selected, null, 2)}</pre>
                </div>
                <div className="modal-footer">
                  <button className="btn btn-secondary" type="button" onClick={() => setSelected(null)}>
                    Close
                  </button>
                </div>
              </div>
            </div>
          </div>
          <div className="modal-backdrop fade show"></div>
        </>
      )}
    </section>
  );
}

export default Activities;