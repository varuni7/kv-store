package save 
import ( "os" )
func SaveData1(path string, data []byte) error {
    fp, err := os.OpenFile(path, os.O_WRONLY|os.O_CREATE|os.O_TRUNC, 0664)
    if err != nil {
        return err
    }
    defer fp.Close()

    _, err = fp.Write(data)
    if err != nil {
        return err
    }
    return fp.Sync() // fsync
}

//fsync is to persist the data , so its accessable even after you close the application and open it again 

