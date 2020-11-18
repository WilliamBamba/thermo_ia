const initialState = {
    count: 23,
    boolNavBar: false,
    temp: 25,
    modalCreationProfil: false,
    modalProfil: false,
    profile: null
};


export default (storage, setStore, globalState) => {
    const store = {
        state: storage,
        'setState': setStore,
        merge: null,
    };

    const onces = [];
    const repetes = [];

    store.merge = (obj) => {
        let newState = { ...store.state, ...obj };
        setStore(newState);
    }

    store.once = (f) => {
        onces.push(f);
    }


    store.start = () => {
        if (globalState.frist) {
            globalState.frist = false;
            onces.forEach(f => f());
            repetes.forEach(e => {
                setInterval(e.f, e.interval);
            })
        }
        
    }


    return store;
};

export {initialState};