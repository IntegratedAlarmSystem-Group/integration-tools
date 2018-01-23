import org.eso.ias.cdb.CdbReader;
import org.eso.ias.cdb.json.CdbJsonFiles;
import org.eso.ias.cdb.json.JsonReader;
import org.eso.ias.dasu.DasuImpl;
import org.eso.ias.dasu.publisher.KafkaPublisher;
import org.eso.ias.dasu.subscriber.KafkaSubscriber;
import org.eso.ias.prototype.input.Identifier;
import org.eso.ias.prototype.input.java.IdentifierType;
import org.eso.ias.supervisor.Supervisor;
import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

import java.io.IOException;
import java.nio.file.FileSystems;
import java.nio.file.Path;
import java.util.Properties;

public class SupervisorDemo {
    public static void main(String[] args) throws IOException {

        String id = "SupervisorID";

        // set log file name
        System.setProperty("log_file_name", SupervisorDemo.class.getSimpleName());
        Logger logger = LoggerFactory.getLogger(SupervisorDemo.class);

        // Build the CDB reader
        Path cdbParentPath = FileSystems.getDefault().getPath(".");
        CdbJsonFiles cdbFiles = new CdbJsonFiles(cdbParentPath);
        CdbReader reader = new JsonReader(cdbFiles);

        // kafka
        KafkaPublisher publisher = KafkaPublisher.apply(id, new Properties());
        KafkaSubscriber subscriber = new KafkaSubscriber(id, new Properties());

        // supervisor
        Identifier supId = new Identifier(id, IdentifierType.SUPERVISOR);
        Supervisor supervisor = new Supervisor(supId, publisher, subscriber, reader, DasuImpl::apply);

        supervisor.start();

        while (true) {
            // run supervisor permanently
        }
    }
}
