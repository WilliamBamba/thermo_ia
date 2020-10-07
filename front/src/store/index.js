const initialState = {
    count: 0,
};


export default (storage, setStore) => {
    const store = {
        state: storage,
        'setState': setStore,
        merge: null,
    };

    store.merge = (obj) => {
        let newState = { ...store.state, ...obj };
        setStore(newState);
    }


    return store;
};

export {initialState};