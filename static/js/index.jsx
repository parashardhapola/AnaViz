class FileInput extends React.Component{
    constructor(props) { 
        super(props);
        this.handleChange = this.handleChange.bind(this);
        this.handleSubmit = this.handleSubmit.bind(this);
    }
    handleChange(event) {
        console.log(this.fileInput.files);
    }
    handleSubmit(event){
        event.preventDefault();
        let formData = new FormData();
        const files = this.fileInput.files;
        for (var key in files) {
            if (files.hasOwnProperty(key) && files[key] instanceof File) {
                formData.append(key, files[key]);
            }   
        }
        axios.post('/fnupload', formData
        ).then(function (response) {
            console.log(response);
        }).catch(function (error) {
            console.log(error);
        });
    }
    render() {
        return (
        <form onSubmit={this.handleSubmit}>
            <input type="file" multiple="true" ref={input => {this.fileInput = input;}}
                   onChange={this.handleChange} />
            <input type="submit" value="Upload" />
        </form>            
        );
    }
}


class AppWrapper extends React.Component {
    render() {
        return (
            <div>
                <p>Please upload <b>barcodes.tsv</b>, <b>genes.tsv</b> and <b>matrix.mtx</b></p>
                <FileInput />
            </div>
        );
    }
}


ReactDOM.render(
    <AppWrapper />, document.getElementById('app')
);
