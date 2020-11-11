const initialState = {
    count: 23,
    boolNavBar: false,
    temp: 25,
    modalCreationProfil: false,
    modalProfil: false,
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