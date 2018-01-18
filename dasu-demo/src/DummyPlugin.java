
import ch.qos.logback.classic.LoggerContext;
import org.eso.ias.plugin.Plugin;
import org.eso.ias.plugin.PluginException;
import org.eso.ias.plugin.config.PluginConfig;
import org.eso.ias.plugin.config.Value;
import org.eso.ias.plugin.publisher.MonitorPointSender;
import org.eso.ias.plugin.publisher.PublisherException;
import org.eso.ias.plugin.publisher.impl.KafkaPublisher;
import org.eso.ias.prototype.input.java.OperationalMode;
import org.slf4j.LoggerFactory;

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.concurrent.ScheduledFuture;
import java.util.concurrent.TimeUnit;

/**
 * publishes data from a weather station to a Kafka Queue
 */
public class DummyPlugin extends Plugin {

    /**
     * runs the plugin.
     */
    public static void main(String[] args) throws IOException {
        System.err.println("Starting dummy plugin...");

        // stop logging
        LoggerContext loggerContext = (LoggerContext) LoggerFactory.getILoggerFactory();
        loggerContext.stop();
        System.err.println("Stopped logging");

        // IASIO
        int refreshTime = 1000;

        // configuration
        PluginConfig config = new PluginConfig();
        config.setId("DummyPlugin");
        config.setMonitoredSystemId("DummyStation");
        config.setSinkServer("localhost");
        config.setSinkPort(9092);

        // values
        Value dummyVal = new Value();
        dummyVal.setId(valueId);
        dummyVal.setRefreshTime(refreshTime);
        config.setValues(new Value[]{dummyVal});

        // publisher
        KafkaPublisher publisher = new KafkaPublisher(config.getId(),
                config.getMonitoredSystemId(),
                config.getSinkServer(),
                config.getSinkPort(),
                Plugin.getScheduledExecutorService());

        // start plugin
        DummyPlugin dummy = new DummyPlugin(config, publisher);
        try {
            dummy.start();
        } catch (PublisherException pe) {
            System.err.println("The plugin failed to start");
            pe.printStackTrace(System.err);
            System.exit(-3);
        }

        // set mode
        dummy.setPluginOperationalMode(OperationalMode.OPERATIONAL);
        dummy.startLoop();
        System.err.println("Plugin started, sending value 0. waiting for user input...");

        // start reading values from input
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        String line;
        while ((line = br.readLine()) != null) {
            try {
                Double value = Double.parseDouble(line);
                dummy.value = value;

                System.err.println("dummy value updated to " + value);
            } catch (Exception e) {
                System.err.println("Invalid value");
            }
        }

        br.close();
        System.err.println("Closing plugin");

        try {
            dummy.loopFuture.get();
        } catch (Exception e) {
            System.err.println("loop terminated");
        }
    }

    /**
     * the loop to keep the plugin running.
     */
    private ScheduledFuture<?> loopFuture;

    private double value;
    private static String valueId = "dummy";

    private DummyPlugin(PluginConfig config, MonitorPointSender sender) {
        super(config, sender);
    }

    /**
     * Override method to catch the exception and log a message
     * <p>
     * In the example we do not take any special action if the Plugin returns an
     * error when submitting a new value.
     */
    @Override
    public void updateMonitorPointValue(String mPointID, Object value) {
        try {
            super.updateMonitorPointValue(mPointID, value);
        } catch (PluginException pe) {
            System.err.println("Error sending " + mPointID + " monitor point to the core of the IAS");
        }
    }

    /**
     * The loop to update the value every 1 second
     */
    private void startLoop() {
        // send data every second.
        loopFuture = getScheduledExecutorService().scheduleAtFixedRate(
                () -> {
                    updateMonitorPointValue(valueId, value);
                }, 0, 1, TimeUnit.SECONDS);
    }
}
