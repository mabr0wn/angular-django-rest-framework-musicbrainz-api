const mock = () => {
    let storage = {};
    return {
        getItem: key => (key in storage ? storage[key] : null),
        setItem: (key, value) => (storage[key] = value || ''),
        removeItem: key => delete storage[key],
        clear: () => (storage = {})
    };
};
// Mocking localStorage && sessionStorage is optional
Object.defineProperty(window, 'localStorage', { value: mock() });
Object.defineProperty(window, 'sessionStorage', { value: mock() });
// without mocking getComputedStyle your test won’t run, 
// as Angular checks in which browser it executes. We need to fake it.
Object.defineProperty(window, 'getComputedStyle', {
    value: () => ['-webkit-appearance']
});